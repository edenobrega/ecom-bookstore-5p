# Generated by Django 3.2.14 on 2022-07-14 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderTime',
            new_name='OrderItem',
        ),
    ]
