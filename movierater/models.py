from django.db import models
from django.utils import timezone

# Create your models here.
GENRE_TYPES = [
    ('ROMANCE','Romance'),
    ('ACTION','Action'),
    ('HORROR','Horror'),
    ('THRILLER','Thriller'),
    ('ENTERTAINMENT', 'Entertainment')
]

RATING = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
] 

class Rater(models.Model):
    error_css_class = "error"
    Movie_Name = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50, choices=GENRE_TYPES) 
    Directed_By= models.CharField(max_length=100)
    Description= models.TextField()
    Rating = models.CharField(max_length=10, choices=RATING, null=True)
    # date = models.DateField(default=timezone.now)


    

