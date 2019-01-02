"""mineral_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from minerals import views

urlpatterns = [
    # index
    path('', views.mineral_list, name='index'),
    # show mineral details
    path('detail/<int:pk>', views.mineral_detail, name='detail'),
    # XC: Show random element
    path('random/', views.random_mineral, name='random'),
    # Django admin
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
