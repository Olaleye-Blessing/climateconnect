# Generated by Django 2.2.13 on 2021-04-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0081_auto_20210427_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationtranslation',
            name='short_description_translation',
            field=models.TextField(blank=True, help_text='Translation of short description', max_length=560, null=True, verbose_name='Short description translation'),
        ),
        migrations.AlterField(
            model_name='projecttranslation',
            name='short_description_translation',
            field=models.TextField(blank=True, help_text="Translation of project's short description", max_length=560, null=True, verbose_name='Short description translation'),
        ),
    ]