# Generated by Django 5.0 on 2023-12-31 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='uploads/')),
                ('edited_video', models.FileField(blank=True, null=True, upload_to='edited_videos/')),
            ],
        ),
    ]