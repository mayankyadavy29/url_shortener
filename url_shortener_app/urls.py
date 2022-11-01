from django.contrib import admin
from django.urls import path
from url_shortener_app import views

app_name = 'url_shortener_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_url, name='create_url'),
    path('detail/<int:url_id>/', views.detail, name='detail'),
    path('delete/<int:url_id>/', views.delete, name='delete'),
    path('cnfrm_delete/<int:url_id>/', views.cnfrm_delete, name='cnfrm_delete'),
    path('view_urls/', views.view_urls, name='view_urls')
]