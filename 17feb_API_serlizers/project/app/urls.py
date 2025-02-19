from django.urls import path
from.import views

urlpatterns = [
    path('stu_list/',views.student_list),
    path('stu_detail/<int:pk>',views.student_details),
]