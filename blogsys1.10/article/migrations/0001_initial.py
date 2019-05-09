# Generated by Django 2.1.5 on 2019-01-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=20, unique=True)),
                ('a_part', models.CharField(default='你猜', max_length=20, null=True)),
                ('a_tag', models.CharField(default='Django', max_length=10, null=True)),
                ('a_date', models.DateTimeField(auto_now_add=True)),
                ('a_load', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
