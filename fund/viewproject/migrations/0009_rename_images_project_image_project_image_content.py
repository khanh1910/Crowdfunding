# Generated by Django 4.1.2 on 2022-11-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0008_project_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Images',
            new_name='Image',
        ),
        migrations.AddField(
            model_name='project',
            name='Image_Content',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
