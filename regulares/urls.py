from django.urls import path
from regulares.views import home

urlpatterns = [
    path(r'', home),
]