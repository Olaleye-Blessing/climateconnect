# Generated by Django 3.2.15 on 2022-10-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0098_organizationtags_hide_get_involved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='get_involved',
            field=models.TextField(blank=True, help_text='How to get involved textfield', max_length=250, null=True, verbose_name='How to get involved'),
        ),
    ]
