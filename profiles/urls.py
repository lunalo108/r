from django.urls import re_path, include

from .views import ProfileRetrieveAPIView


urlpatterns = [

    re_path(r'', ProfileRetrieveAPIView.as_view(), name='edit_user'),
    
]