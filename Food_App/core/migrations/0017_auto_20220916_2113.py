# Generated by Django 3.2.14 on 2022-09-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220916_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='core.Review'),
        ),
    ]
