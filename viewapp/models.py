from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    division = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
