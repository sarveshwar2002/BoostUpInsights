from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Consistent lowercase naming and added trailing slash
    path('services/', views.services, name='services'),  # Added trailing slash
    path('about/', views.about, name='about'),  # Added trailing slash
    path('contact/', views.contact, name='contact'),  # Added trailing slash
    path('blogs/', views.blogs, name='blogs'),
    path('BlogTemplate1/', views.BlogTemplate1, name='Template1'),
    path('BlogTemplate2/', views.BlogTemplate2, name='Template2'),
    path('BlogTemplate3/', views.BlogTemplate3, name='Template3')

]
