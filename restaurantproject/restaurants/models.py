from django.db import models
from datetime import datetime

# def validate_indian_standard_time(value):
#         ist_start = timezone.make_aware(timezone.datetime(2000, 1, 1, 0, 0, 0), timezone.get_current_timezone())
#         ist_end = timezone.make_aware(timezone.datetime(2000, 1, 1, 23, 59, 59), timezone.get_current_timezone())

#         if not ist_start <= value <= ist_end:
#             raise ValidationError("Time must be in Indian Standard Time (IST) range (00:00:00 - 23:59:59).")

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    

    def __str__(self):
        return self.name
    
    
   