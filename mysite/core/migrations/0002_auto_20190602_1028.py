# Generated by Django 2.1.2 on 2019-06-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
    ]