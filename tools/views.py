from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from tools.models import Tool, CATEGORY_CHOICES
from .forms import ToolForm

from django.views.generic import ListView, DetailView
# ---------------------------
# Submit a Tool
# ---------------------------
def submit_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tools:list')  # ✅ must exist in urls.py
    else:
        form = ToolForm()

    return render(request, 'tools/submit_tool.html', {
        'form': form,
    })


# ---------------------------
# Tool List (with filters)
# ---------------------------
class ToolListView(ListView):
    model = Tool
    template_name = 'tools/tool_list.html'
    context_object_name = 'tools'
    paginate_by = 24

    def get_queryset(self):
        qs = Tool.objects.all()
        category = self.request.GET.get('category')  # direct string from query param
        pricing = self.request.GET.get('pricing')
        sort = self.request.GET.get('sort')
        search = self.request.GET.get('search')

        if category:
            qs = qs.filter(category=category)  # ✅ now it's a CharField

        if pricing:
            qs = qs.filter(pricing=pricing)

        if search:
            qs = qs.filter(name__icontains=search) | qs.filter(description__icontains=search)

        if sort == 'upvotes':
            qs = qs.order_by('-upvotes')
        elif sort == 'created':
            qs = qs.order_by('-created_at')

        return qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ✅ CATEGORY_CHOICES is now a tuple of choices, not a queryset
        context['categories'] = [c[0] for c in CATEGORY_CHOICES]  
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_pricing'] = self.request.GET.get('pricing', '')
        return context


# ---------------------------
# Upvote a Tool
# ---------------------------
@require_POST
@login_required
def upvote_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)

    if request.user in tool.upvoted_by.all():
        return JsonResponse({'error': 'Already upvoted', 'upvotes': tool.upvotes})

    tool.upvotes += 1
    tool.upvoted_by.add(request.user)
    tool.save()
    return JsonResponse({'upvotes': tool.upvotes})

class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'  # create this template
    context_object_name = 'tool'
# ---------------------------
# Signup View
# ---------------------------
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ---------------------------
# About Us Page
# ---------------------------
def aboutus(request):
    return render(request, "about.html")
from django.shortcuts import render, get_object_or_404
from .models import Tool, CATEGORY_CHOICES
from django.utils.text import slugify
from django.http import Http404

# ---------------------------
# Individual Category Pages
# ---------------------------
def productivity_tools(request):
    """Productivity Tools Category Page"""
    return category_page_view(request, 'Productivity', 'productivity-tools.html')

def marketing_tools(request):
    """Marketing Tools Category Page"""
    return category_page_view(request, 'Marketing', 'marketing-tools.html')

def design_tools(request):
    """Design Tools Category Page"""
    return category_page_view(request, 'Design', 'design-tools.html')

def ai_art_tools(request):
    """AI Art Tools Category Page"""
    return category_page_view(request, 'AI Art', 'ai-art-tools.html')

def web_development_tools(request):
    """Web Development Tools Category Page"""
    return category_page_view(request, 'Web Development', 'web-development-tools.html')

def writing_tools(request):
    """Writing Tools Category Page"""
    return category_page_view(request, 'Writing', 'writing-tools.html')

def education_tools(request):
    """Education Tools Category Page"""
    return category_page_view(request, 'Education', 'education-tools.html')

def data_analysis_tools(request):
    """Data Analysis Tools Category Page"""
    return category_page_view(request, 'Data Analysis', 'data-analysis-tools.html')

def automation_tools(request):
    """Automation Tools Category Page"""
    return category_page_view(request, 'Automation', 'automation-tools.html')

def cybersecurity_tools(request):
    """Cybersecurity Tools Category Page"""
    return category_page_view(request, 'Cybersecurity', 'cybersecurity-tools.html')

def category_page_view(request, category_name, template_name):
    """Generic function to handle individual category pages"""
    # Check if category exists in choices
    valid_categories = [choice[0] for choice in CATEGORY_CHOICES]
    if category_name not in valid_categories:
        raise Http404("Category not found")
    
    # Get tools for this category
    tools = Tool.objects.filter(category=category_name)
    
    # Add filtering options
    pricing = request.GET.get('pricing')
    sort = request.GET.get('sort')
    search = request.GET.get('search')

    if pricing:
        tools = tools.filter(pricing=pricing)

    if search:
        tools = tools.filter(name__icontains=search) | tools.filter(description__icontains=search)

    if sort == 'upvotes':
        tools = tools.order_by('-upvotes')
    elif sort == 'created':
        tools = tools.order_by('-created_at')
    else:
        tools = tools.order_by('-upvotes')  # Default sort by upvotes

    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(tools, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get related categories
    related_categories = []
    for choice in CATEGORY_CHOICES:
        if choice[0] != category_name and Tool.objects.filter(category=choice[0]).exists():
            related_categories.append({
                'name': choice[0],
                'count': Tool.objects.filter(category=choice[0]).count()
            })
    
    # Get category stats
    total_tools = Tool.objects.filter(category=category_name).count()
    free_tools = Tool.objects.filter(category=category_name, pricing='Free').count()
    premium_tools = Tool.objects.filter(category=category_name, pricing='Premium').count()
    freemium_tools = Tool.objects.filter(category=category_name, pricing='Freemium').count()
    
    context = {
        'category_name': category_name,
        'tools': page_obj,
        'page_obj': page_obj,
        'categories': [c[0] for c in CATEGORY_CHOICES],
        'search_query': request.GET.get('search', ''),
        'selected_pricing': request.GET.get('pricing', ''),
        'selected_sort': request.GET.get('sort', 'upvotes'),
        'related_categories': related_categories[:6],
        'total_tools': total_tools,
        'free_tools': free_tools,
        'premium_tools': premium_tools,
        'freemium_tools': freemium_tools,
    }
    
    return render(request, f'categories/{template_name}', context)


class CategoryListView(ListView):
    model = Tool
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # Get all categories with tool counts
        categories_with_counts = []
        for choice in CATEGORY_CHOICES:
            category_name = choice[0]
            tool_count = Tool.objects.filter(category=category_name).count()
            if tool_count > 0:  # Only show categories that have tools
                categories_with_counts.append({
                    'name': category_name,
                    'count': tool_count,
                    'slug': category_name.lower().replace(' ', '-').replace('/', '-')
                })
        
        # Sort by tool count (most popular first)
        return sorted(categories_with_counts, key=lambda x: x['count'], reverse=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_categories'] = len(self.get_queryset())
        return context
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout(request):
    logout(request)
    return redirect('login')  # or redirect('/') for homepage
def sitemap(request):
    return render(request,"sitemap.xml")
def robots(request):
    return render(request,"robots.txt")
