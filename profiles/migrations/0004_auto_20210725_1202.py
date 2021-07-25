# Generated by Django 3.2.4 on 2021-07-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210723_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='email',
            new_name='default_email',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='default_first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_name',
            new_name='default_last_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='town_or_city',
            new_name='default_town_or_city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postcode',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]