# Generated by Django 4.0.2 on 2022-02-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate', '0002_teammate_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammate',
            name='title',
            field=models.CharField(default='Mr.', max_length=10),
        ),
    ]
