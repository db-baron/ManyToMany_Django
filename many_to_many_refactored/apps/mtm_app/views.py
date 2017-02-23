from django.shortcuts import render, redirect
from .models import User, Interest
from django.db.models import Count

# Create your views here.
def index(request):
    return render (request, 'mtm_app/index.html')

def add_user(request):
    if User.objects.validateUser(request.POST):

        return redirect("/showResults")
    else:
        return redirect("/")
    # return redirect('/showinterest')
def showResults(request):
    context ={
    'users' : User.objects.all()
    }
    return render(request, 'mtm_app/results.html', context)

def showInterest(request, id):
    user = User.objects.filter(id=id)
    context = {
        'profile' : user[0].interests.all()
    }
    return render(request, 'mtm_app/interests.html', context)

def deleteInterest(request, id):
    Interest.objects.get(id=id).delete()
    return redirect("/showResults")

def deleteUser(request, id):
    User.objects.get(id=id).delete()
    # remove_user = User.objects.get(id=id)
    # remove_user.delete()
    return redirect("/showResults")
