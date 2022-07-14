from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher (models.Model):
    teacher = models.ForeignKey(User,  on_delete=models.CASCADE)
    language = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=20, null=False)
    isApproved=models.BooleanField(default=False)

class ExamCategory (models.Model):
    categoryName=models.CharField(max_length=50, unique=True, default="Ilets")

class Exam (models.Model):
    type = models.CharField(max_length=50, null=False)
    level = models.PositiveIntegerField(max_length=2, null=False)
    name = models.CharField(max_length=60, unique=True)
    teacher = models.ForeignKey(User,related_name="+",on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    final_grade = models.PositiveIntegerField(max_length=2, default=10)
    examCategory=models.ForeignKey(ExamCategory,related_name='+',on_delete=models.CASCADE)

class Question (models.Model):
    question = models.CharField(max_length=500, null=False)
    correctAnswer = models.CharField(max_length=200, null=False)
    answer_1 = models.CharField(max_length=200, null=False)
    answer_2 = models.CharField(max_length=200, null=False)
    answer_3 = models.CharField(max_length=200, null=False)
    exam = models.ForeignKey(Exam, related_name='+', null=False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Student (models.Model) :
    student_Account = models.ForeignKey(User,related_name='+',on_delete=models.CASCADE)
    country = models.CharField(max_length=20, null=False)
    userPhotoPath=models.CharField(max_length=200, null=False, default="")

class Student_Grade ( models.Model ):
    grade = models.PositiveIntegerField(max_length=2, null=False)
    exam = models.ForeignKey(Exam,related_name='+',on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='+', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
class Comments ( models.Model ):
    comment = models.CharField(max_length=1000, null=False)
    exam = models.ForeignKey(Exam, related_name='+',on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

class Task (models.Model):
    student = models.ForeignKey(Student, related_name='+',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='+',on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=False)
    grade = models.CharField(max_length=3,null=False)
