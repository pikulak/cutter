# Generated by Django 2.0.4 on 2018-04-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='sha256',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]