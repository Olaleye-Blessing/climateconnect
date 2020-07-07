# Generated by Django 2.2.13 on 2020-07-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0015_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='explanation',
            field=models.CharField(blank=True, help_text="Explanation of the role's permissions for the user", max_length=256, null=True, verbose_name='Explanation'),
        ),
    ]