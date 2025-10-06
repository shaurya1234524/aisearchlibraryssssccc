from django.urls import path
from .views import (ToolListView, upvote_tool, CategoryListView, 
                   productivity_tools, marketing_tools, design_tools, 
                   ai_art_tools, web_development_tools, writing_tools,
                   education_tools, data_analysis_tools, automation_tools,
                   cybersecurity_tools,logout)
from tools import views

app_name = 'tools'

urlpatterns = [
    path('', ToolListView.as_view(), name='list'),
    path('<int:pk>/', views.ToolDetailView.as_view(), name='detail'),
    path('upvote/<int:pk>/', upvote_tool, name='upvote'),
        path('logout/', logout,name='logout'),

    # Category List URL
    path('categories/', CategoryListView.as_view(), name='category_list'),
    
    # Individual Category Pages
    path('productivity-tools/', productivity_tools, name='productivity_tools'),
    path('marketing-tools/', marketing_tools, name='marketing_tools'),
    path('design-tools/', design_tools, name='design_tools'),
    path('ai-art-tools/', ai_art_tools, name='ai_art_tools'),
    path('web-development-tools/', web_development_tools, name='web_development_tools'),
    path('writing-tools/', writing_tools, name='writing_tools'),
    path('education-tools/', education_tools, name='education_tools'),
    path('data-analysis-tools/', data_analysis_tools, name='data_analysis_tools'),
    path('automation-tools/', automation_tools, name='automation_tools'),
    path('cybersecurity-tools/', cybersecurity_tools, name='cybersecurity_tools'),
]
