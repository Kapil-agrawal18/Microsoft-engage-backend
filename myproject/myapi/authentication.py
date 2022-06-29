from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
import cv2 as cv
import face_recognition
from .views import *


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print("Mein pahunch gaya !")
        username = request.GET.get('username')
        image = request.GET.get('image')
        # password = request.GET.get('password')
        password = False
        if not username:
            return None

        if not image:
            return None
        else:
            # Check image is True or False
            img_url = user.image_url.url
            img_url = img_url.replace("/", "\\")
            img_url = r"C:\Users\tanma\Desktop\Microsoft\rest-api2" + img_url
            
            img = cv.imread(img_url)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(img)[0]

            user = User.objects.get(username=username)
            profile = AppUsers.objects.get(name = user)
            if(face_recognition.compare_faces([img_encoding], profile.encoding)[0]):
                return (user, None)
            else:
                raise exceptions.AuthenticationFailed('Image not matching')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        
        return (user, None)