# Generated by Django 3.2.4 on 2021-07-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
