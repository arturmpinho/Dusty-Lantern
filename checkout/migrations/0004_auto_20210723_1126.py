# Generated by Django 3.2.4 on 2021-07-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='lname',
            new_name='last_name',
        ),
    ]