# Generated by Django 3.0.2 on 2020-01-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
