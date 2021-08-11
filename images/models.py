import os
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.urls import reverse
from urllib.request import urlretrieve
from django.core.files import File

from PIL import Image as Img


class Image(models.Model):
    image = models.ImageField(
        upload_to='images/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name='Файл'
    )
    formatted_image = models.ImageField(
        upload_to='images/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name='Отформатированное изображение'
    )
    image_url = models.URLField(blank=True, null=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Изображение'

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})

    def get_remote_image(self):
        if self.image_url and not self.image:
            result = urlretrieve(self.image_url)
            with open(result[0], 'rb') as f:
                image = File(f)
                self.image.save(
                    os.path.basename(self.image_url),
                    image
                )
                self.save()

    def change_size(self, width, height):
        if self.image:
            size = self._get_new_size(width, height)
            with BytesIO() as buffer:
                img = Img.open(self.image.path)
                img = img.resize(size, Img.ANTIALIAS)
                img.save(buffer, 'JPEG')
                buffer.seek(0)
                self.formatted_image = SimpleUploadedFile(
                    name=f'{self.image.name}_resized.jpeg',
                    content=buffer.read(),
                    content_type='image/jpeg'
                )

    def _get_new_size(self, width, height):
        if not width:
            width = height

        if not height:
            height = width

        width_ratio = width / self.image.width
        height_ratio = height / self.image.height

        if width_ratio < height_ratio:
            new_width = width
            new_height = round(width_ratio * self.image.height)
        else:
            new_width = round(height_ratio * self.image.width)
            new_height = height

        return (new_width, new_height)

    def __str__(self):
        return self.image.name.split('/')[-1]

