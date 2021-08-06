from django import forms

from images.models import Image


class ImageUploadForm(forms.Form):
    image_url = forms.URLField(label='Ссылка', required=False)
    image_input = forms.ImageField(label='Файл', required=False)

    def clean(self, *args, **kwargs):
        pass

