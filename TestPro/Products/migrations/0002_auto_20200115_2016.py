# Generated by Django 3.0.2 on 2020-01-15 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='email',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='no',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
