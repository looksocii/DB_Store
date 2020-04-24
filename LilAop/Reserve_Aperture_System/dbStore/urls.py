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
    path('add_company/<int:aperture_id>/', views.add_company, name='add_company'),
    path('store_detail_edit/<int:store_id>/', views.store_detail_edit, name='store_detail_edit'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
    path('sale_view/<int:aper_id>/', views.sale_view, name='sale_view'),
    path('add_store/', views.add_store, name='add_store'),
    path('remove_store/<int:store_id>/', views.remove_store, name='remove_store'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)