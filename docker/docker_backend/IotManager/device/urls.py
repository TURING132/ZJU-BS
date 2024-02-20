from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add),
    path('get', views.get),
    path('modify', views.modify),
    path('get_message', views.get_message)
]