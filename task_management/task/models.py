from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField('category.Category',related_name='task_categories')
    description = models.TextField()
    assign_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title