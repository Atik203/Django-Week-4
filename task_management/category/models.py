from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    task = models.ManyToManyField('task.Task', related_name='category_tasks')

    def __str__(self):
        return self.name