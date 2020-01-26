from django.db import models


class ToDoList(models.Model):
    name=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


