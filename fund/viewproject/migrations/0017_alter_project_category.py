# Generated by Django 4.1.2 on 2022-12-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0016_alter_project_content_alter_project_shortdescribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Category',
            field=models.CharField(choices=[('Công Nghệ', 'Công nghệ'), ('Dịch Vụ', 'Dịch vụ'), ('Du Lịch', 'Du lịch'), ('Nông Nghiệp', 'Nông nghiệp'), ('Giáo Dục', 'Giáo dục')], default='', max_length=20),
        ),
    ]