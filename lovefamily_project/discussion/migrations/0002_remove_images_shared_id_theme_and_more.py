# Generated by Django 4.0.6 on 2022-07-14 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images_shared',
            name='id_theme',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='id_theme',
        ),
        migrations.RemoveField(
            model_name='videos_shared',
            name='id_theme',
        ),
        migrations.DeleteModel(
            name='discussionTheme',
        ),
    ]
