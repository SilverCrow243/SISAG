"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import dashboard
from ministries.views import ministries_list,ministries_detail
from projects.views import projects_list, project_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"), 
    path('ministries-list/', ministries_list, name="ministries_list"), 
    path('ministries-detail/<int:pk>/', ministries_detail, name='ministries_detail'), 
    path('project-list/', projects_list, name="projects_list"), 
    path('project-detail/<int:pk>/', project_detail, name='project_detail'), 


    path('', dashboard, name="dashboard"),
]
