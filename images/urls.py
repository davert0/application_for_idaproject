from django.urls import path

from images.views import HomeView, UploadImageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload_image/', UploadImageView.as_view(), 'upload_image')
]
