from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# POST creation 
class Instruction(models.Model):
  User_Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Name')
  id = models.BigAutoField(primary_key=True)
  Category_M = models.CharField(max_length=100,null=True,primary_key=False)
  Title_M   = models.CharField(max_length=200,null=True,primary_key=False)
  Details_M = RichTextField(null=True)
  Likes_M = models.ManyToManyField(User, related_name='blog_Post',blank=True)
  Liked_int_M = models.IntegerField(default='0')
  ImagesM  = models.FileField(blank=True, upload_to='images/')
  published_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.Title_M 

  
  def get_absolute_url(self):
    return reverse('display')



# Category Field 
class Category(models.Model):
  Category_Field = models.CharField(max_length=200,null=True)
  published_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.Category_Field
    


# POST comment 
class Comment(models.Model):
  User_Name = models.ForeignKey(User, on_delete=models.CASCADE)
  post_ID   = models.ForeignKey(Instruction, on_delete=models.CASCADE,default=0)
  Comment = models.TextField(max_length=2000,null=True)
  Commented_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.Comment


# User-INFO 
class User_Information(models.Model):
  User_Name = models.OneToOneField(User, on_delete=models.CASCADE, default='1')
  First_name = models.CharField(max_length=200,blank=True)
  Last_name = models.CharField(max_length=200,blank=True)
  PAN_ID_Number = models.CharField(max_length=10,null=True)
  Adhar_Card_Number = models.CharField(max_length=16,null=True)
  Mobile_Number = models.CharField(max_length=10,null=True)
  Instagram = models.CharField(max_length=200,blank=True)
  Facebook = models.CharField(max_length=200,blank=True)
  LindedIN = models.CharField(max_length=200,blank=True)
  AboutU = models.TextField(max_length=200,blank=True)  
  Photo  = models.FileField(blank=True, upload_to='UserImage/')
  Update_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.First_name



# Google ADDS 
class GoogleAdd(models.Model):
  Display = models.BooleanField(default=True)
  id = models.BigAutoField(primary_key=True)
  Company_name = models.CharField(max_length=100,blank=True)
  ADD  = models.FileField(blank=True, upload_to='Google_ADDs/')
  Company_url = models.CharField(max_length=500,blank=True)
  published_date = models.DateTimeField(default=timezone.now)
  Clicking = models.ManyToManyField(User, related_name='clicking', blank=True)
  
  def __str__(self):
    return self.Company_name
    


