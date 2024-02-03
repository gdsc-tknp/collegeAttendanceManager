from django.db import models

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    phone = models.TextField()
    name = models.CharField(max_length=100)
    school_id_number = models.TextField()
