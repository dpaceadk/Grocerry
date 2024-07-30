from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Groceries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null =True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()

