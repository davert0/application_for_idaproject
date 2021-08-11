from django.shortcuts import render

from django.views.generic import ListView, FormView, DetailView, UpdateView

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


def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            url = form.cleaned_data.get('image_url')
            image = form.cleaned_data.get('image_input')
            if image:
                img_obj = Image(image=image)
                img_obj.save()
            if url:
                img_obj = Image(image_url=url)
                img_obj.get_remote_image()
                img_obj.save()
    else:
        form = ImageUploadForm()
    context = {
        'form': form
    }
    return render(request, 'images/upload.html', context)

