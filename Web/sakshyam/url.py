from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.all, name='menu'),
    path('buy/<int:chai_id>/', views.buy_chai, name='buy_chai'),
     path('description/<int:chai_id>/', views.view_description, name='view_description'),
]