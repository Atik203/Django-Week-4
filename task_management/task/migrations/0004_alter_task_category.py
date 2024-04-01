# Generated by Django 5.0.3 on 2024-04-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category_task'),
        ('task', '0003_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(related_name='task_categories', to='category.category'),
        ),
    ]