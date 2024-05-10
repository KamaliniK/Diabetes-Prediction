from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),  # Mapping the root URL to the home view
    path("predict/", views.predict),
    path("predict/result", views.result),
]
