"""
URL configuration for e_scorer project.

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
from scoring.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',admin_login,name='admin_login'),
    path('judges/login',judge_login,name='judge_login'),

    #event urls
    # path('events/create/',create_event,name='create_event'),
    # path('events/delete/<int:event_id>',delete_event,name='delete_event'),
    # path('events/manage/',manage_event,name='manage_event'),
    # path('events/update/<int:event_id>/',update_event,name='update_event'),

    #performer urls
    path('performers/',performer_list,name='performer_list'),
    # path('performers/create/',performer_create,name='performer_create'),
    # path('performers/update/<int:id>/',performer_update,name='performer_update'),
    # path('performers/delete/<int:id>/',performer_delete,name='performer_delete'),

    #judge urls
    # path('judges/',judge_list,name='judge_list'),
    # path('judges/create/',judge_create,name='judge_create'),
    # path('judges/update/<int:id>/',judge_update,name='judge_update'),
    # path('judges/delete/<int:id>/',judge_delete,name='judge_delete'),
    path('judges/score/<int:id>/', judge_score, name='judge_score'),

]
