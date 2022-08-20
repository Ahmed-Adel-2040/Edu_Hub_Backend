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
        data = []
        error = "No Error"
        status=200
        dataJson={}
        try:
            CategoryList = ExamCategory.objects.filter(categoryName=Category)
            AllExam=Exam.objects.filter(examCategory_id=CategoryList.first().id)
            AllExam = list(AllExam)
            if len(AllExam)==0:
                status=404
                raise Exception("this Category not found ")

            if str(Response.status_code).startswith("5"):
                error = 'it is the internal server error  ' + Response.status_text

            for element in AllExam:
                data.append(element.name)

            dataJson = {"status": Response.status_code,
                        "error": error,
                        "data": data}
            return Response(dataJson)
        except Exception as e:
            dataJson = {"status": status,
                        "error": str(e),
                        "data": ""}
            return Response(dataJson)

    @api_view(["Get"])
    def getExamByCategoryAndName(self,Category,name):
        data = []
        error = "No Error"
        dataJson={}
        status=200
        try:
            CategoryList = ExamCategory.objects.filter(categoryName=Category)
            AllExam = Exam.objects.filter(examCategory_id=CategoryList.first().id)

            AllExam = list(AllExam)
            flage = 0
            examObject = {}
            for exam in AllExam:
                if exam.name==name:
                    examObject["type"] = exam.type
                    examObject["finalGrade"] = exam.final_grade
                    Questions = serializers.serialize('json',Question.objects.filter(exam_id=exam.id), fields=( 'question',))
                    # if exam.type!="choose":

                    examObject["Questions"] = Questions
                    Questions = Question.objects.filter(exam_id=exam.id)
                    Questions=list(Questions)
                    AllAnswersLists=[]

                    for Quest in Questions:
                        answerList = []
                        if exam.type=="choose":
                            answerList.append(Quest.pk)
                            answerList.append(Quest.answer_1)
                            answerList.append(Quest.answer_2)
                            answerList.append(Quest.answer_3)
                        else:
                            answerList.append(Quest.pk)
                            answerList.append(Quest.answer_1)

                        AllAnswersLists.append(answerList)
                    examObject["Answers"]=AllAnswersLists


                    flage = 1

                    break
            if flage == 0:
                Response.status_code = 404
                raise Exception ("this exam name not found")


            if str(Response.status_code).startswith("4"):
                error = 'it is the user input  error  ' + Response.status_text

            dataJson = {"status": Response.status_code,
                        "error": error,
                        "data": examObject}
            return Response(dataJson )
        except Exception as e:

            error=str(e)
            dataJson = {"status": Response.status_code,
                        "error": error,
                        "data": ""}
            return Response(dataJson)

    @api_view(["GET"])
    def getExamAnswers(self,Category,name):
        data = []
        error = "No Error"
        dataJson = {}
        status = 200
        try:
            CategoryList = ExamCategory.objects.filter(categoryName=Category)
            AllExam = Exam.objects.filter(examCategory_id=CategoryList.first().id)

            AllExam = list(AllExam)
            flage = 0
            examObject = {}
            for exam in AllExam:
                if exam.name == name:
                    examObject["type"] = exam.type
                    examObject["finalGrade"] = exam.final_grade
                    Questions = serializers.serialize('json', Question.objects.filter(exam_id=exam.id),
                                                      fields=('question',"correctAnswer",))
                    examObject["Questions"] = Questions
                    flage = 1
                    print(Questions)
            if flage == 0:
                Response.status_code = 404
                raise Exception("this exam name not found")

            if str(Response.status_code).startswith("4"):
                error = 'it is the user input  error  ' + Response.status_text

            dataJson = {"status": Response.status_code,
                        "error": error,
                        "data": examObject}
            return Response(dataJson)
        except Exception as e:

            error = str(e)
            dataJson = {"status": Response.status_code,
                        "error": error,
                        "data": ""}
            return Response(dataJson)
