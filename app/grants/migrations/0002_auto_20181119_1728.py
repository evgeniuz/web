# Generated by Django 2.1.2 on 2018-11-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='frequency',
            field=models.DecimalField(decimal_places=0, default=0, help_text='The payout frequency of the Grant.', max_digits=50),
        ),
    ]
