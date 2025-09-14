from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils import timezone



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first=models.CharField("First Name",max_length=30)
    last=models.CharField("Last Name",max_length=30)
    about=models.CharField("About Me",max_length=300,blank=True,null=True)
    image=models.ImageField("Your Image",upload_to='media',null=True,blank=True ,default="user.jpg")
    address=models.CharField(max_length=50,blank=True,null=True)
    work=models.CharField("Work Hours Number",max_length=2,blank=True,null=True)
    waiting_time=models.IntegerField("Waiting Time ",blank=True,null=True)
    price=models.IntegerField("Price Of Photo Session",null=True,blank=True)
    join_us=models.DateTimeField("Time Of Join",auto_now_add=True,blank=True,null=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    twitter=models.CharField(max_length=100,blank=True,null=True)
    google=models.CharField(max_length=100,blank=True,null=True)
    slug=models.SlugField("slug",blank=True,null=True)

       

    def __str__(self):
        return self.first
    # def create_profile(sender,**kwargs):
    #     if kwargs['created']:
    #         Profile.objects.create(user=kwargs['instance'])   

    # post_save.connect(create_profile,sender=User)   

# class Image(models.Model):
#     caption=models.CharField(max_length=40)
#     img=models.ImageField(upload_to='media/')
#     def __str__(self):
#         return self.caption

class project(models.Model):

    grapher = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    discription = models.CharField(max_length=40)
    work = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.discription 


class Contact(models.Model):
    user = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first