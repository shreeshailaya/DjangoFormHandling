from django.contrib import admin
from .models import PostModel,UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(PostModel)
