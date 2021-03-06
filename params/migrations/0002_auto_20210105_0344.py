# Generated by Django 3.1.4 on 2021-01-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='params',
            name='genre',
            field=models.CharField(choices=[('modern_love', 'Modern Love'), ('modern_mythology_folklore', 'Modern Mythology'), ('modern_nature', 'Modern Nature'), ('renaissance_love', 'Renaissance Love'), ('renaissance_mythology_folklore', 'Renaissance Mythology'), ('renaissance_nature', 'Renaissance Nature')], default='Modern Love', max_length=120),
        ),
        migrations.AlterField(
            model_name='params',
            name='syls',
            field=models.CharField(default='5-7-5', max_length=120, verbose_name='Syllable Scheme (e.g. 5-7-5 for a haiku)'),
        ),
    ]
