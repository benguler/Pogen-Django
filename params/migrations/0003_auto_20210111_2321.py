# Generated by Django 3.1.4 on 2021-01-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0002_auto_20210105_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='params',
            name='syls',
            field=models.CharField(default='5-7-5', max_length=120, verbose_name='Syllable Scheme'),
        ),
    ]
