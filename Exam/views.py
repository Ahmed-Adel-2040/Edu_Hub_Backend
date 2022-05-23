from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import  api_view
# Create your views here.

class ExamViews():
    @api_view(["Get"])
    def getAllCategory(self):
        CategoryList=ExamCategory.objects.order_by('categoryName')

        CategoryList = list(CategoryList)
        data=[]
        error ="No Error"
        if str(Response.status_code).startswith("5"):
            error='it is the internal server error  '+Response.status_text
        elif str(Response.status_code).startswith("4"):
            error='it is the user input  error  '+Response.status_text

        for element in CategoryList:
            data.append(element.categoryName)

        dataJson={"status":Response.status_code,
                  "error":error,
                  "data":data}
        return  Response(dataJson)

    @api_view(["Get"])
    def getExamByCategory(self,Category):
        CategoryObject=get_object_or_404(ExamCategory,categoryName=Category)
        #CategoryList = ExamCategory.objects.filter(categoryName=Category)
        AllExam=Exam.objects.filter(examCategory_id=CategoryObject.id)
        AllExam=list(AllExam)

        #return Response(data)

