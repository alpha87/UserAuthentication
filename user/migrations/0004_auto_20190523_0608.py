# Generated by Django 2.1.5 on 2019-05-23 06:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190523_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='increase',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]