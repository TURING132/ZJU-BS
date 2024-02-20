# Generated by Django 3.2.22 on 2023-12-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('normal', 'Normal'), ('location', 'Location'), ('warning', 'Warning')], default='normal', max_length=10),
        ),
    ]