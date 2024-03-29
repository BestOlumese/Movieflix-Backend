# Generated by Django 4.2.9 on 2024-01-23 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
                ('short_synopsis', models.TextField(max_length=500)),
                ('full_synopsis', models.TextField(max_length=500)),
                ('rating', models.CharField(max_length=250)),
                ('movie_quality', models.CharField(choices=[('720p', '720p'), ('1080p', '1080p'), ('2k', '2k'), ('4k', '4k')], max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('year_released', models.CharField(max_length=500)),
                ('image', models.ImageField(max_length=500, upload_to='uploads/movies/% Y/% m/% d/')),
                ('youtube_url', models.CharField(max_length=500)),
                ('netflix_url', models.CharField(blank=True, max_length=500)),
                ('prime_url', models.CharField(blank=True, max_length=500)),
                ('genre', models.CharField(max_length=500)),
                ('date_created', models.DateField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Category.category')),
            ],
        ),
    ]
