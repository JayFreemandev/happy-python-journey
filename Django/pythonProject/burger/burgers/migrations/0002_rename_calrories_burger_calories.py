# Generated by Django 4.2.6 on 2023-10-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burgers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burger',
            old_name='calrories',
            new_name='calories',
        ),
    ]