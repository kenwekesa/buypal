"""buypal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from . import views as mainviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainviews.home, name="homepage"),
    path("buypal-crypto", mainviews.page_details_view, name="page-details"),
    path("login", mainviews.login_view, name="login"),
    path("signup", mainviews.signup_view, name="signup"),
    path("user-home", mainviews.userdashboard_view, name="user-home"),
    path('scrape/', mainviews.scrape, name="scrape"),
     path("news", mainviews.news_view, name="news"),
     path("stockexchange", mainviews.stockexchange_view, name="stock-exchange"),
     path("viewnews", mainviews.view_news_view, name="read-news"),
     path("updatenews", mainviews.get_news_view, name="update-card-news"),
     path('logout/', auth_views.LogoutView.as_view(template_name = 'buypal/index.html'), name='logout'),
     path('user-profile-update', mainviews.edit_profile_view,name='update-profile'),

]
