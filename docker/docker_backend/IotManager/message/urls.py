from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post),
    path('location_list', views.location_list),
    path('location_history', views.location_history)
]