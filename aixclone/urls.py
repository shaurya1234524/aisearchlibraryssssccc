from django.urls import path,include
from tools.views import ToolListView, submit_tool,signup_view
from django.contrib import admin
app_name = 'tools'
from tools import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
        # ... your normal URLs ...
     path('', ToolListView.as_view(), name='list'),
    path('submit/', views.submit_tool, name='submit'),
        path('sitemap.xml',views.sitemap,name="sitemap"),
 path('robots.txt',views.robots,name="robots"),
path('admin/',admin.site.urls),
      path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   path('signup/', signup_view, name='signup'),  # <-- add this
    path('', include('tools.urls', namespace='tools')),
    path('aboutus/',views.aboutus,name="aboutus"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

