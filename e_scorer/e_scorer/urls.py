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
from scoring.views import admin_login,create_event,delete_event,manage_event,update_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',admin_login,name='admin_login'),
    path('events/create/',create_event,name='create_event'),
    path('events/delete/<int:event_id>',delete_event,name='delete_event'),
    path('events/manage/',manage_event,name='manage_event'),
    path('events/update/<int:event_id>/',update_event,name='update_event'),
]
