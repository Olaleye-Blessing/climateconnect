# Generated by Django 2.2.11 on 2020-04-14 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0010_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Comment content', verbose_name='Content')),
                ('is_abusive', models.BooleanField(default=False, help_text='If comment is abusive', verbose_name='Is abusive?')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when post was created', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when comment was updated', verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Time when comment was deleted', null=True, verbose_name='Deleted at')),
                ('author_user', models.ForeignKey(help_text='Points to user who made comment', on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Author User')),
                ('deleted_by_user', models.ForeignKey(blank=True, help_text='Person who deleted the comment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_delete', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by user')),
                ('post', models.ForeignKey(help_text='Points to post a comment was made to', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='organization.Posts', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Post Comments',
            },
        ),
    ]
