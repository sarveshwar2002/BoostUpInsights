from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),  # Consistent lowercase naming and added trailing slash
]
