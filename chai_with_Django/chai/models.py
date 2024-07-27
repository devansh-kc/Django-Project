from django.db import models
from django.utils import timezone 

# Create your models here.
class ChaiVariety(models.Model):
    Chai_Type=[
        ("ST","Sex Tea"),
        ("PST","Tea with angela white and ava addams's squirt"),
        ("NL","Normal tea"),
        ("SL","Normal tea"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_field = models.DateTimeField(default=timezone.now)
    tea_type = models.CharField(max_length=3,choices=Chai_Type)
    description = models.TextField(default="")
    

def __str__(self):
    return self.name
