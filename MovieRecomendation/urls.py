from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendations/', include('recommendations.urls')),  # Inclui as URLs do aplicativo recommendations
]
