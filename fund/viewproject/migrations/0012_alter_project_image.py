# Generated by Django 4.1.2 on 2022-12-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0011_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Image',
            field=models.ImageField(null=True, upload_to='project'),
        ),
    ]
