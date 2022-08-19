from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Curation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='Curation', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    loc_tag = models.TextField()

    def __str__(self):
        return self.loc_tag

class Category(models.Model):
    cat_tag = models.TextField()

    def __str__(self):
        return self.cat_tag

class Purpose1(models.Model):
    pur_tag = models.TextField()
    
    def __str__(self):
        return self.pur_tag

class Purpose2(models.Model):
    pur_tag= models.TextField()

    def __str__(self):
        return self.pur_tag

class Place(models.Model):
    place = models.CharField(max_length=200)
    info = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    open = models.TextField(null=True, blank=True)
    number = models.TextField(null=True, blank=True)
    sns = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    loc = models.ForeignKey('Location', on_delete=models.CASCADE)
    cat = models.ForeignKey('Category',on_delete=models.CASCADE)
    pur1 = models.ForeignKey('Purpose1', on_delete=models.CASCADE, null=True, blank=True)
    pur2 = models.ForeignKey('Purpose2', on_delete=models.CASCADE, null=True, blank=True)
    latlng = models.TextField(null=True, blank=True) #위경도

    def __str__(self):
        return self.place