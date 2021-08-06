"""szkolenie URL Configuration

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
from rest_framework.urlpatterns import format_suffix_patterns
from modelszkolenie import views

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),
    # Linki
    path('',views.home, name='home'),
    # Linki do api restframework
    path('api/company', views.CompanyList.as_view()),
    path('api/company/<int:pk>', views.CompanyDetail.as_view()),
    path('api/user/', views.UserList.as_view()),
    path('api/user/<int:pk>', views.UserDetail.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
