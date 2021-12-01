# Generated by Django 2.2.20 on 2021-07-27 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0065_userprofile_email_on_idea_join'),
        ('climate_match', '0003_userquestionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Translated text for the question', max_length=1024, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when question was first translated', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when question was updated', verbose_name='Updated at')),
                ('language', models.ForeignKey(help_text='Points to a language we will translate question to', on_delete=django.db.models.deletion.CASCADE, to='climateconnect_api.Language', verbose_name='Language')),
                ('question', models.ForeignKey(help_text='Points to question that will be translated', on_delete=django.db.models.deletion.CASCADE, related_name='translate_question', to='climate_match.Question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Question translation',
                'verbose_name_plural': 'Question translations',
            },
        ),
        migrations.CreateModel(
            name='AnswerTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Translated text for answers', max_length=1024, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when answer was first translated', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when answer was updated', verbose_name='Updated at')),
                ('answer', models.ForeignKey(help_text='Points to answer translation', on_delete=django.db.models.deletion.CASCADE, related_name='translate_answer', to='climate_match.Answer', verbose_name='Answer')),
                ('language', models.ForeignKey(help_text='Points to a language we will translate answer to', on_delete=django.db.models.deletion.CASCADE, to='climateconnect_api.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Answer translation',
                'verbose_name_plural': 'Answer translations',
            },
        ),
    ]