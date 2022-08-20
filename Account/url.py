from django.urls import path
from . import views
urlpatterns = [
    path('user/<str:userName>/<str:passWord>', views.UserViews.getUserData,name="user"),

    ]