# Generated by Django 4.2.16 on 2024-11-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vlogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vlogpost',
            options={'ordering': ['-published_date']},
        ),
    ]