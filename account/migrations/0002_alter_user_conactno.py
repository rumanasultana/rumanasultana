# Generated by Django 3.2.6 on 2021-10-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='conactno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
