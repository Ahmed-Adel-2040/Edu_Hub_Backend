from rest_framework import serializers
from .models import *

class ExamSerializer(serializers.ModelSerializer):
    class Mete:
        model = Exam
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Mete:
        model = Student
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Mete:
        model = Teacher
        fields = '__all__'
class ExamCategorySerializer(serializers.ModelSerializer):
    class Mete:
        model = ExamCategory
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Mete:
        model = Question
        fields = '__all__'

class Student_GradeSerializer(serializers.ModelSerializer):
    class Mete:
        model = Student_Grade
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Mete:
        model = Comments
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Mete:
        model = Task
        fields = '__all__'
