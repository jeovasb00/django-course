from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    gender = {
        "M": "Male",
        "F": "Famale",
        "O": "Other"
    }
    email = models.EmailField()

    def __str__(self):
        return self.name