# Generated by Django 5.0.1 on 2024-01-23 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('member', 'book')},
        ),
    ]
