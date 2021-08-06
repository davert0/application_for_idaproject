from django.shortcuts import render

from django.views.generic import ListView, FormView

from images.forms import ImageUploadForm
from images.models import Image


class HomeView(ListView):
    model = Image
    template_name = 'images/index.html'
    context_object_name = 'images'


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

# class UploadImageView(FormView):
#     template_name = 'images/upload.html'
#     form_class = ImageUploadForm
#
#     success_url = '/'
#     def form_valid(self, form):
#         return super().form_valid(form)
