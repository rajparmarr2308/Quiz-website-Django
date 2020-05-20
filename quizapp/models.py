from django.db import models
import datetime
from django.utils import timezone
class question(models.Model):
    question=models.CharField(max_length=100)
    def __str__(self):
        return self.question

class choice(models.Model):
    question=models.ForeignKey(question,on_delete=models.CASCADE)        
    choice_text=models.CharField(max_length=20)

    
    
    def __str__(self):
        return self.choice_text
