from django.db import models
from datetime import datetime

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=20, default = '')
    date = models.DateField(default=datetime.now)
    ISBN = models.CharField(max_length=17, default = '') #ISBN is a 13-digit bar code for publication identification
    pages = models.IntegerField(default = 0) #number of pages of book
    
    
    def __str__(self):
        return self.title
