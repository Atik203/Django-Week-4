# Generated by Django 5.0.3 on 2024-04-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='task',
            field=models.ManyToManyField(related_name='categories', to='task.task'),
        ),
    ]