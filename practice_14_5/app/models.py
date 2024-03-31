from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    SUBJECT = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Flask', 'Flask'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('JavaScript', 'JavaScript'),
    )
    subject = models.CharField(max_length=50, choices=SUBJECT)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} - {self.roll} - {self.city} - {self.subject} - {self.birthday} - {self.email} - {self.phone}'