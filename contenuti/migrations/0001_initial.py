# Generated by Django 3.0.5 on 2020-04-10 05:12

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('published', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('originale', models.FileField(default='', upload_to='video/originale/')),
                ('video_480', models.FileField(blank=True, null=True, upload_to='video/mp4_480')),
                ('video_720', models.FileField(blank=True, null=True, upload_to='video/mp4_720')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
