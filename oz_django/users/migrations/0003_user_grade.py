# Generated by Django 5.1.4 on 2024-12-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(default='C', max_length=10),
        ),
    ]
