from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

PET_CHOICES = (
               ("Cat","Cat"),
               ("Dog","Dog"),
               ("Bird","Bird"),
               ("Other","Other")
              )

class Pet(models.Model):
    pet_type = models.CharField(max_length=100,choices=PET_CHOICES)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True,null=True)
    pounds = models.DecimalField(max_digits=10,decimal_places=2)

    def __unicode__(self):
        return self.name

## Feel free to change these as you see fit, but please update on the profile template page.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_owner = models.BooleanField()
    is_sitter = models.BooleanField()
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=30,blank=True,null=True)
    zip_code = models.IntegerField(blank=True,null=True)
    pets = models.ManyToManyField(Pet,blank=True,null=True)
    tagline = models.CharField(max_length=40,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    sit_cats = models.BooleanField()
    sit_dogs = models.BooleanField()
    sit_birds = models.BooleanField()
    sit_other = models.BooleanField()
    qualifications = models.TextField(blank=True,null=True)
    not_willing_to_sit = models.TextField(blank=True,null=True)
    concerns = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Appointment(models.Model):
    owner = models.ForeignKey(User,related_name="owner")
    sitter = models.ForeignKey(User,related_name="sitter")
    datetime = models.DateTimeField()
    owner_rating = models.IntegerField(blank=True,null=True)
    owner_review = models.TextField(blank=True,null=True)
    sitter_rating = models.IntegerField(blank=True,null=True)
    sitter_review = models.TextField(blank=True,null=True)
