"""diagxpert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hello import views
from hello.views import FeedbackCreateView
# from .views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("contacts/", views.contacts),
    path("person/", views.person),
    path("person/postuser/", views.postuser),
    path("picture/", views.picture),
    path("authorization/", views.login_view),
    path("registration/", views.form_registration),
    path("registration/success/", views.registration_success),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
