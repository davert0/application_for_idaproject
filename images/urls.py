from django.urls import path

from images.views import HomeView, upload_image_view, ImageDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_image/', upload_image_view, name='upload_image'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
]
