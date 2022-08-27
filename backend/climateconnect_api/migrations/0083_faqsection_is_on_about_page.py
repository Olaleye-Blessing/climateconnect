# Generated by Django 3.2.14 on 2022-07-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0082_auto_20220419_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqsection',
            name='is_on_about_page',
            field=models.BooleanField(default=False, help_text='Identifies the section that should be shown on the about page faq section', verbose_name='Is shown on about page'),
        ),
    ]