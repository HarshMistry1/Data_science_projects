# Generated by Django 2.2.5 on 2022-01-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatdata',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
