"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from project import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),

    # Auth
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser'),

    # Project
    path('', views.home,name='home'),
    path('create/',views.createproject,name='createproject'),
    path('current/',views.currentprojects,name='currentprojects'),
    path('project/<int:project_pk>',views.viewproject,name='viewproject'),
    path('project/<int:project_pk>/delete',views.deleteproject,name='deleteproject'),
    path('project/<int:project_pk>/complete',views.completeproject,name='completeproject'),
    path('complete/',views.completeprojects,name = 'completeprojects'),
]
