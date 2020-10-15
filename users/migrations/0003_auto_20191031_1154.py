# Generated by Django 2.2.5 on 2019-10-31 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191015_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], default='krw', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], default='kr', max_length=2),
        ),
    ]
