# Generated by Django 4.2.9 on 2024-01-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=10)),
                ('value_sell', models.DecimalField(decimal_places=2, max_digits=15)),
                ('value_buy', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
