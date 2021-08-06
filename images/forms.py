from django.forms import ModelForm

from images.models import Image


class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

