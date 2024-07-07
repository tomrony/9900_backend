"""
URL configuration for comp9900 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import login,signup,main_page
from heatmap.views import covid_data
from dashboard.views import charts_data


urlpatterns = [
    path('', main_page),
    # path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('heatmap/', covid_data, name='heatmap'),
    path('charts/', charts_data, name='charts'),


]
