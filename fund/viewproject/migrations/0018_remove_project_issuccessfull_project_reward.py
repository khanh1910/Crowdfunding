# Generated by Django 4.1.2 on 2022-12-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0017_alter_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='IsSuccessfull',
        ),
        migrations.AddField(
            model_name='project',
            name='Reward',
            field=models.CharField(default='', max_length=60),
        ),
    ]