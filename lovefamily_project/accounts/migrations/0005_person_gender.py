# Generated by Django 4.0.6 on 2022-07-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_person_partner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='male', max_length=6),
        ),
    ]
