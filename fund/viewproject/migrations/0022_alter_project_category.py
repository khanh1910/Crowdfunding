# Generated by Django 4.1.2 on 2022-12-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0021_rename_content_project_content1_project_content2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Category',
            field=models.CharField(choices=[('CN', 'Công nghệ'), ('DV', 'Dịch vụ'), ('DL', 'Du lịch'), ('NN', 'Nông nghiệp'), ('GD', 'Giáo dục')], default='', max_length=20),
        ),
    ]