# Generated by Django 3.2.4 on 2021-06-30 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210630_0604'),
        ('auctions', '0003_auto_20210630_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='Image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.image'),
        ),
    ]