# Generated by Django 2.0.4 on 2018-04-25 09:49

from django.db import migrations, models
import django.db.models.deletion
import files.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileAudio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sha256', models.CharField(blank=True, max_length=60)),
                ('upload', models.FileField(blank=True, upload_to=files.models.processed_audio_file_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TempFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sha256', models.CharField(blank=True, max_length=60)),
                ('upload', models.FileField(upload_to=files.models.temp_file_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fileaudio',
            name='temp_file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='files.TempFile'),
        ),
    ]
