from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    for student in Student.objects.all():
        if student.teacher:
            student.teachers.add(student.teachers)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    # students = Student.objects.all()
    students = Student.objects.prefetch_related('teachers')
    context['students'] = students

    return render(request, template, context)
