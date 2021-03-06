# Generated by Django 2.1.3 on 2018-12-09 20:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='用户评论')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
                'ordering': ['-comment_time'],
            },
        ),
        migrations.CreateModel(
            name='UserFavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_thumb_up', models.BooleanField(default=False, verbose_name='点赞与否')),
                ('favor_created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.CharField(max_length=500, verbose_name='消息内容')),
                ('message_send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('message_nums', models.IntegerField(verbose_name='消息量')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='UserVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_nums', models.IntegerField(verbose_name='阅读')),
            ],
            options={
                'verbose_name': '用户访问',
                'verbose_name_plural': '用户访问',
            },
        ),
    ]
