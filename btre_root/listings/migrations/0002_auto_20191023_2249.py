# Generated by Django 2.2.6 on 2019-10-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrom',
            field=models.DecimalField(decimal_places=1, default=2, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
    ]
