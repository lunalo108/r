from .views import quotes_table
from django.urls import re_path, include

urlpatterns = [

    re_path(r'', quotes_table),
    
]