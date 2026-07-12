from django.shortcuts import render
from .models import Student, Result

def home(request):
    student = None
    results = None
    error = None

    if request.method == "POST":
        roll_number = request.POST.get("roll_number")

        try:
            student = Student.objects.get(roll_number=roll_number)
            results = Result.objects.filter(student=student)
        except Student.DoesNotExist:
            error = "Student not found."

    return render(request, "home.html", {
        "student": student,
        "results": results,
        "error": error,
    })
