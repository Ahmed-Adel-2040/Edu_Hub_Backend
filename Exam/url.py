from django.urls import path
from . import views
urlpatterns = [
    path('', views.ExamViews.getAllCategory,name="home"),
    path('Category/<str:Category>', views.ExamViews.getExamByCategory,name="ExamCategory"),

]