# Generated by Django 4.1.5 on 2023-06-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='otp',
            field=models.BigIntegerField(null=True),
        ),
    ]