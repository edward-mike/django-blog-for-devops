# Generated by Django 5.0.3 on 2024-03-29 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ('created_date',), 'verbose_name': 'Post Board', 'verbose_name_plural': 'Post Boards'},
        ),
    ]
