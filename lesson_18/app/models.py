from django.db import models
from datetime import datetime 
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField("publicated time",default=datetime.now)
# auto_now_add=True
    def __str__(self):
        return self.title
    




    