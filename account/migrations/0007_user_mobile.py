# Generated by Django 4.1.1 on 2022-09-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_first_name_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
