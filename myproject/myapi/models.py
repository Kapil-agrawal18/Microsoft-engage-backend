from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
   return 'images/{filename}'.format(filename = filename)

def upload_to_detected(instance, filename):
   return 'images_detected/{filename}'.format(filename = filename)

def upload_video_to_detected(instance, filename):
   return 'videos_detected/{filename}'.format(filename = filename)

class Criminals(models.Model):
   id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   name = models.CharField(max_length=100)
   image_url = models.ImageField(upload_to = upload_to, null = True, blank = True)
   crimes = models.CharField(max_length=100, null = True, blank = True)
   encoding = models.CharField(max_length=5000, null=True, blank = True)
   current_status = models.CharField(max_length=100, null = True, blank = True)

class CriminalImgDetect(models.Model):
   name = models.CharField(max_length=100, blank = True, null = True)
   query_image_url = models.ImageField(upload_to = upload_to_detected, null = True, blank = True)
   image_url = models.ImageField(null = True, blank = True)
   crimes = models.CharField(max_length=100, null = True, blank = True)
   encoding = models.CharField(max_length=5000, null=True, blank = True)
   current_status = models.CharField(max_length=100, null = True, blank = True)

class CriminalVideoDetect(models.Model):
   query_video_url = models.FileField(upload_to = upload_video_to_detected, null = True, blank = True)
   name = models.CharField(max_length=100, blank = True, null = True)


class AppUsers(models.Model):
   id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   department = models.CharField(max_length=100, blank = True, null = True)
   image_url = models.ImageField(null = True, blank = True)
   encoding = models.CharField(max_length=5000, null=True, blank = True)
   password = models.CharField(max_length=100, blank = True, null = True)
   last_video_url = models.CharField(max_length=500, blank = True, null = True)
   last_image_url = models.CharField(max_length=500, blank = True, null = True)