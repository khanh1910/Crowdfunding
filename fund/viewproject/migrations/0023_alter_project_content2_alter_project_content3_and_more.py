# Generated by Django 4.1.2 on 2022-12-04 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewproject', '0022_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Content2',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Content3',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Content4',
            field=models.TextField(default='', null=True),
        ),
    ]