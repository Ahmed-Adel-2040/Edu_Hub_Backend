from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.core import serializers
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
        #CategoryObject=get_object_or_404(ExamCategory,categoryName=Category)
        CategoryList = ExamCategory.objects.filter(categoryName=Category)
        AllExam=Exam.objects.filter(examCategory_id=CategoryList.first().id)
        AllExam = list(AllExam)
        data = []
        error = "No Error"
        if str(Response.status_code).startswith("5"):
            error = 'it is the internal server error  ' + Response.status_text
        elif str(Response.status_code).startswith("4"):
            error = 'it is the user input  error  ' + Response.status_text

        for element in AllExam:
            data.append(element.name)

        dataJson = {"status": Response.status_code,
                    "error": error,
                    "data": data}
        return Response(dataJson)

    @api_view(["Get"])
    def getExamByCategoryAndName(self,Category,name):
        # CategoryObject=get_object_or_404(ExamCategory,categoryName=Category)
        CategoryList = ExamCategory.objects.filter(categoryName=Category)
        AllExam = Exam.objects.filter(examCategory_id=CategoryList.first().id)
        examObject={}
        AllExam = list(AllExam)
        for exam in AllExam:
            if exam.name==name:
                examObject["type"]=exam.type
                examObject["finalGrade"]=exam.final_grade
                Questions=serializers.serialize('json',Question.objects.filter(exam_id=exam.id), fields=('question', 'answer_1','answer_2','answer_3',))
                #Questions=Question.objects.filter(exam_id=exam.id)

                examObject["Questions"]=Questions
                print(Questions)
        data = []
        error = "No Error"
        if str(Response.status_code).startswith("5"):
            error = 'it is the internal server error  ' + Response.status_text
        elif str(Response.status_code).startswith("4"):
            error = 'it is the user input  error  ' + Response.status_text



        dataJson = {"status": Response.status_code,
                    "error": error,
                    "data": examObject}
        return Response(dataJson )

