from django.urls import path

from images.views import HomeView, ImageDetailView, ImageUploadView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_image/', ImageUploadView.as_view(), name='upload_image'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
]
