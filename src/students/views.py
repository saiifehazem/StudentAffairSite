from django.shortcuts import render, redirect, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student
from django.urls import reverse

from django.shortcuts import render, redirect


def index(request):
    # Logic for the "Home" link
    return render(request, 'index.html')


def student_info(request):
    # Logic for the "search students" link
    return render(request, 'studentInfo.html')


def add_student(request):
    # Logic for the "Add New Student" link
    return render(request, 'addStudent.html')


def view_status(request):
    # Logic for the "View Status" link
    return render(request, 'allStatus.html')


def sign_out(request):
    # Logic for the "Sign Out" link
    # Perform any sign out actions if needed
    return redirect('index')  # Redirect to the home page


def studentList(request):
    allStudents = Student.objects.all()  # Get all students from the database
    context = {'allStudents': allStudents}
    return render(request, 'studentList.html', context)


def studentData(request):
    allStudents = Student.objects.all()  # Get all students from the database
    # Store all students in a dictionary
    # { 'FrontEnd Name': returned value from the database }
    context = {'allStudents': allStudents}
    # Pass the students to the template
    # 'students/studentList.html',
    return render(request, 'studentData.html', context)


def studentUpdate(request):
    return render(request, 'studentUpdate.html')


def studentDepart(request):
    return render(request, 'studentDepart.html')


def studentAddition(request):
    return render(request, 'studentAddition.html')


def studentInfo(request, id):
    studentInfo = Student.objects.get(id=id)
    context = {'studentInfo': studentInfo}
    return render(request, 'studentInfo.html', context)


def student_detail_view(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }
    return render(request, 'studentInfo.html', context)


def assign_department(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        department = request.POST.get('dep')
        student.department = department
        student.save()
        return HttpResponseRedirect(reverse('students:studentInfo', args=[student.id]))
    context = {'student': student}
    return render(request, 'studentDepart.html', context)


def assign_status(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        department = request.POST.get('status')
        student.status = status
        student.save()
        return HttpResponseRedirect(reverse('students:studentInfo', args=[student.id]))
    context = {'student': student}
    return render(request, 'studentList.html', context)


def save_status(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                student = Student.objects.get(id=student_id)
                student.status = value
                student.save()
        # Replace 'students' with the appropriate URL pattern name for displaying the student list
        return redirect('students')
    # Replace 'status.html' with the actual template name
    return render(request, 'studentList.html')
