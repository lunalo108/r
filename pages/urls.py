from django.urls import path

from . import views

urlpatterns = [
    path('',views.my_first_view),
    path('123',views.my_second_view),
]