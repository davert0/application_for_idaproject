from django.shortcuts import render

from django.views.generic import ListView, FormView

from images.forms import ImageUploadForm
from images.models import Image


class HomeView(ListView):
    model = Image
    template_name = 'images/index.html'
    context_object_name = 'images'


class UploadImageView(FormView):
    template_name = 'images/upload.html'
    form_class = ImageUploadForm

    # success_url = '/thanks/'
    #
    def form_valid(self, form):
        return super().form_valid(form)