from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

