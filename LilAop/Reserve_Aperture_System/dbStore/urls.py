from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.my_register, name='register'),
    path('aperture/', views.aperture, name='view_aperture'),
    path('store_detail/<int:store_id>/', views.store_detail, name='store_detail'),
    path('aperture_detail/<int:aperture_id>/', views.aperture_detail, name='aperture_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)