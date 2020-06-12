from django.db import models
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
