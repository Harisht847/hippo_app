from django.shortcuts import render, redirect
from hippo_app.forms import MigrationForm, MigrationForm2
from .models import SourceDB

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MigrationForm(request.POST)
        form2 = MigrationForm2(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password  = form.cleaned_data.get("password")
                print(username)
                print(password)
        
                messages.success(request, "New Success")
                return redirect("/home")
        else:
            messages.error(request, "Invalid please try again")
    else:
        form = MigrationForm()
        form2 = MigrationForm2()
    return render(request, 'hippo_app/home.html', {"form":form, "form2":form2})


def main_view(request):
    qs = SourceDB.objects.all()
    for q in qs:
        print(q.name)
    render(request, 'hippo_app/main.html', {'qs':qs})
    return render(request, 'hippo_app/main.html', {'qs':qs} )


def form2(request):
    if request.method == 'POST':
        form = MigrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'New success!')
            return redirect("/form2")
        else:
            messages.error(request, 'Invalid Please try again.')
    else:
        form = MigrationForm()
    return render(request, 'hippo_app/form2.html', {'form':form})