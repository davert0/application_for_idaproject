from django.db import models
from django.urls import reverse


class Image(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})
