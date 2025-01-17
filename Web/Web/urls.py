from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.SignUppage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('item/', include('sakshyam.url')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('feedback/', views.feedback_view, name='feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
