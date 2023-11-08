from django.db import models
from datetime import datetime

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    

    def __str__(self):
        return self.name
    
    
   