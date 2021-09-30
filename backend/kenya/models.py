from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# class Contact(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     contact_details = models.EmailField(blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image', blank=True,null=True)

    def __str__(self) -> str:
       return self.name


class Sport(models.Model):
    sport_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
       return self.sport_name


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=50,null=True,blank=True)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    sport = models.ForeignKey(Sport, on_delete=models.DO_NOTHING,null=True)
    profile_email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.user.username

@receiver(post_save, sender = User)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

    for user in User.objects.all():
        Token.objects.get_or_create(user = user)
