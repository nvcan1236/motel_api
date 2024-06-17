# Generated by Django 5.0.4 on 2024-05-01 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_comment_updated_date_alter_like_updated_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForRent',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('ward', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('other_address', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('post.post',),
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]