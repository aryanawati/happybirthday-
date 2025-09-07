from django.db import models

# Create your models here.
class Birthday(models.Model):
    email = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.birthday}"