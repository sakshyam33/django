from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.all, name='menu'),
    path('add/<int:chai_id>/', views.add_to_cart, name='add_cart'),
    path('description/<int:chai_id>/', views.view_description, name='view_description'),
    path('cart/',views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/update/<int:chai_id>/', views.update_cart, name='update_cart'),
    path('feedback/', views.feedback_view, name='feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)