import pytest
from io import BytesIO
from PIL import Image as img

from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from images.models import Image

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def fake_image():
    image_file = BytesIO()
    image = img.new('RGBA', size=(400, 500), color=(256, 0, 0))
    image.save(image_file, 'png')
    image_file.seek(0)

    return SimpleUploadedFile(name='test.png', content=image_file.read())


@pytest.mark.parametrize(
    'size, expected', [
        ((200, 200), (160, 200)),
        ((300, 400), (300, 375)),
        ((800, 600), (480, 600))
    ]
)
def test_image_model_get_new_size(size, expected, fake_image, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    image = Image()
    image.image = fake_image

    size = image._get_new_size(*size)

    assert size == expected


@pytest.mark.parametrize(
    'size', [
        ((200, 200)),
        ((200, 0)),
        ((0, 200))
    ]
)
def test_model_change_size(fake_image, size, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    image = Image()
    image.image = fake_image
    image.save()

    image.change_size(*size)

    assert image.formatted_image.url is not None


def test_upload_image_with_url(tmp_path):
    settings.MEDIA_ROOT = tmp_path
    image = Image()
    image.image_url = 'https://i.picsum.photos/id/515/536/354.jpg?hmac=sqBk5kFg1TmOgauWvn96Op46NjGQ-Hv07aIon4zHsE8'

    image.save()

    assert image.image.url is not None
