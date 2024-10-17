from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('add/', views.photo_add_page, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit/', views.photo_edit_page, name='photo-edit'),
        path('delete/', views.photo_delete_page, name='photo-delete'),
    ]))
]
