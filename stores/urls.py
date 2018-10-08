from django.urls import path
from . import views

urlpatterns = [
    path('<int:store_id>/browse', views.browse, name='browse'),
]
