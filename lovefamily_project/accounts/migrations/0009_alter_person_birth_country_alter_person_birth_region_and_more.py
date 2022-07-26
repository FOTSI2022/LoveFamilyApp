# Generated by Django 4.0.6 on 2022-07-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_country',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_region',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='history',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]