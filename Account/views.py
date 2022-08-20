from django.shortcuts import render
from Exam.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.contrib.auth.models import User
#from django.contrib.auth.hashers import

from passlib.hash import pbkdf2_sha256
#from passlib.handlers.pbkdf2 import d
# Create your views here.
class UserViews():
    @api_view(["GET"])
    def getUserData(self,userName,passWord):
        decpassword=pbkdf2_sha256.hash(passWord, rounds= 216000, salt=b'PXBkgL')
        #decpassword=hashlib.md5(passWord.encode()).hexdigest()
        #pbkdf2_sha256.
        print(pbkdf2_sha256.verify("12345", decpassword))
        print(decpassword)
        userObject=User.objects.filter(username__exact=userName,password__exact=decpassword)
        userObject=list(userObject)
        if len(userObject)==0:
            return Response(data="not authrized")

        return Response(data="ok")
