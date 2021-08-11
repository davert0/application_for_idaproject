from django.urls import reverse

from django.views.generic import ListView, UpdateView, CreateView

from images.forms import ImageUploadForm, ImageChangeForm
from images.models import Image


class HomeView(ListView):
    model = Image
    template_name = 'images/index.html'
    context_object_name = 'images'


class ImageDetailView(UpdateView):
    model = Image
    form_class = ImageChangeForm
    template_name = 'images/detail.html'
    context_object_name = 'image'

    def get_success_url(self) -> str:
        return self.request.path

    def form_valid(self, form):
        height = form.cleaned_data.get('height', 0)
        width = form.cleaned_data.get('width', 0)

        image = form.instance
        image.change_size(width, height)

        return super().form_valid(form)


class ImageUploadView(CreateView):
    template_name = 'images/upload.html'
    form_class = ImageUploadForm
    model = Image

    def get_success_url(self):
        return reverse('image_detail', kwargs={'pk': self.object.pk})
