from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="images/profile/")


    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail= models.ImageField(null=True, blank=True,upload_to="images/")
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='General')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet = models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | '+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

