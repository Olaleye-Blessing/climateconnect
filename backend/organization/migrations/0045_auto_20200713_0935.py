# Generated by Django 2.2.13 on 2020-07-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0044_auto_20200709_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationtags',
            options={'ordering': ['id'], 'verbose_name': 'Organization Tags'},
        ),
    ]