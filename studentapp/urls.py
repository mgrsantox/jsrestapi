from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage),
    path('api/', Get_students_List.as_view()),
    path('api/<int:pk>/', Delete_students_List.as_view()),
]
