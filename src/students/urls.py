from django.shortcuts import redirect, render
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView as login, LogoutView


app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.studentData, name='studentData'),
    path('add/', views.studentAddition, name='add'),
    path('status/', views.studentList, name='status'),
    path('update-status/', views.updateStudentStatus, name='update-status'),

    path('login/', login.as_view(template_name='login.html'), name='login'),
    path('<int:id>/', views.studentInfo, name='studentInfo'),
    path('update/<int:id>/', views.studentUpdateByID, name='studentUpdateByID'),

    path('assigndep/', views.studentDepart),
    path('students/<int:id>/', views.student_detail_view, name='studentInfo'),
    path('assign-department/<int:id>/',
         views.assign_department, name='assign-department'),
    path('searchResults/', views.search_results, name='searchResults'),
    path('delete/<int:student_id>/', views.delete_student, name='delete'),

]
