# Generated by Django 2.2.24 on 2021-09-08 04:42

import climate_match.models.questions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate_match', '0005_answer_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, help_text='Points to question image', null=True, upload_to=climate_match.models.questions.upload_question_image, verbose_name='Image'),
        ),
    ]