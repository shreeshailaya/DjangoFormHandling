from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class PostModel(models.Model):
    userModel = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
