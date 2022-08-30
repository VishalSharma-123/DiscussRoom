from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic =  models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)           #form can be submitted empty
    participants = models.ManyToManyField(User, related_name = 'participants', blank = True)
    upated = models.DateTimeField(auto_now=True)                        #every save timestamp
    created = models.DateTimeField(auto_now_add=True)                   #first save timestamp
    
    class Meta:
        ordering = ['-upated', '-created']                              #order by date upadted, then by created 
        
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)          #models.SET_NULL = message will stay stay in db, CASCADe deletes everythin
    body = models.TextField()
    upated = models.DateTimeField(auto_now=True)                        
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-upated', '-created']
    
    def __str__(self):
        return self.body[0:50]