# Generated by Django 3.2.6 on 2021-08-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
            ],
        ),
    ]