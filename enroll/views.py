from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           email= fm.cleaned_data['email']
           passw = fm.cleaned_data['password3']

    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {"form":fm})