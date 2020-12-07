# Generated by Django 2.2 on 2020-12-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField()),
                ('time_high', models.DateTimeField()),
                ('time_low', models.DateTimeField()),
                ('open_price', models.DecimalField(decimal_places=15, max_digits=30)),
                ('high_price', models.DecimalField(decimal_places=15, max_digits=30)),
                ('low_price', models.DecimalField(decimal_places=15, max_digits=30)),
                ('close_price', models.DecimalField(decimal_places=15, max_digits=30)),
                ('volume', models.DecimalField(decimal_places=15, max_digits=30)),
                ('market_cap', models.DecimalField(decimal_places=15, max_digits=30)),
            ],
        ),
    ]
