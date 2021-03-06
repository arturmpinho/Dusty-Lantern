# Generated by Django 3.2.4 on 2021-07-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210723_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='town_or_city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_postcode',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
