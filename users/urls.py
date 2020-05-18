from django.urls import re_path, include

from .views import RegistrationAPIView
from .views import LoginAPIView
# from .views import user_login
from .views import LogoutAPIView

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),

    re_path(r'^logout/?$', LogoutAPIView.as_view(), name='user_logout'),
    # re_path(r'', user_login, name='user'),
    re_path(r'', RegistrationAPIView.as_view(), name='user'),
]