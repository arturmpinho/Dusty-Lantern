# Generated by Django 3.2.4 on 2021-07-24 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid_auction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
                ('bid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid')),
            ],
        ),
    ]
