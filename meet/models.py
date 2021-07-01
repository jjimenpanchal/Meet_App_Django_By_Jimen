from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=400)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
        email=models.EmailField(unique=True)
    
        def __str__(self):
            return self.email


class Meet(models.Model):
    organizer_email=models.EmailField()
    date=models.DateField()
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    Participants=models.ManyToManyField(Participant,blank=True,null=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'

