# Generated by Django 3.2.4 on 2021-06-30 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='final_amount',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='number_of_bids',
        ),
    ]
