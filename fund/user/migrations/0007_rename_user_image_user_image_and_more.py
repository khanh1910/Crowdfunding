# Generated by Django 4.1.2 on 2022-11-30 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_Image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='User_Money',
            new_name='Money',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='User_Phone',
            new_name='Phone',
        ),
    ]