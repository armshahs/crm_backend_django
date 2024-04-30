"""
URL configuration for djangoCRM project.

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
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("djoser.urls")),  # S-added for Djoser auth
    path("api/v1/", include("djoser.urls.authtoken")),  # S-added for Djoser auth
    path("api/v1/", include("lead.urls")),  # S-added for lead app
    path("api/v1/", include("team.urls")),  # S-added for team app
    path("api/v1/", include("client.urls")),  # S-added for client app
]
