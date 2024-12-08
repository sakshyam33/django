from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.all, name='menu'),
     path('add/<int:chai_id>/', views.add_to_cart, name='add_cart'),
     path('description/<int:chai_id>/', views.view_description, name='view_description'),
]