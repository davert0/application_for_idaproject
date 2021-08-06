import os
import tempfile
import urllib

from django.db import models
from django.urls import reverse
from urllib.request import urlretrieve
from django.core.files import File


class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True, verbose_name='Файл')
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

    def __str__(self):
        return self.image.name.split('/')[-1]

