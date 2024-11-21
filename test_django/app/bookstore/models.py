from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    
