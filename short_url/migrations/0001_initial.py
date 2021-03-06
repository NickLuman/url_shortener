# Generated by Django 3.1.1 on 2020-09-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.URLField(unique=True)),
                ('hash_url', models.URLField(unique=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
