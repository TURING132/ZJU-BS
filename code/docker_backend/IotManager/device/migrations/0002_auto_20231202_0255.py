# Generated by Django 2.2.12 on 2023-12-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
