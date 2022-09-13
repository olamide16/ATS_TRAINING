from distutils.command.upload import upload
from email import message
from email.mime import image
from os import link
from pydoc import describe
from pyexpat import model
from turtle import heading, update
from django.db import models

# Create your models here.
# #hOME
# class Home(models.Model):
#     name = models.CharField(max_length=20)
#     career = models.CharField(max_length=50)
#     profile_img = models.ImageField(upload_to= 'picture/')
#     update = models.DateTimeField(auto_now=True)
    
#     def __str__(self) -> str:
#         return self.name

# #Abou me

# class About(models.Model):
#     heading = models.CharField(max_length=50)
#     decrip = models.CharField(max_length=100)
#     sub_heading1 = models.CharField(max_length=50)
#     description1 = models.CharField(max_length=150)
#     profile_img1 = models.ImageField(upload_to = 'picture/')
#     sub_heading2 = models.CharField(max_length=50)
#     description2 = models.CharField(max_length=350)
#     profile_img2 = models.ImageField(upload_to = 'picture/')
#     update = models.DateTimeField(auto_now=True)
#     def __str__(self) -> str:
#         return self.heading


# class more_description(models.Model):
#     heading = models.CharField(max_length=50)
#     description = models. CharField(max_length=150)
#     sub_heading = models.CharField(max_length=20)
#     sub_heading2 = models.CharField(max_length=20)
#     sub_heading3 = models.CharField(max_length=20)
#     sub_heading4 = models.CharField(max_length=20)
#     update = models.DateTimeField(auto_now=True)
    
#     def __str__(self) -> str:
#         return self.heading
#     pass

# class Work(models.Model):
#     description = models.CharField(max_length=20)
#     image = models.ImageField(upload_to='picture/')
#     project_link = models.URLField(max_length=200)
    
#     def __str__(self) -> str:
#         return self.description

# class contact(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=20)
#     subject = models.CharField(max_length=50)
#     message = models.CharField(max_length=20)
    
#     def __str__(self) -> str:
#         return self.name
    