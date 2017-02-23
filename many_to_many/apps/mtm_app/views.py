from django.shortcuts import render
from .models import User, Interests
from django.db.models import Count

# Create your views here.
def index(request):
    return render (request, 'mtm_app/index.html')

def formProcess(request):
    User.objects.validateUser(name = request.POST['name'], interest = request.POST['interest'])

    # x = User.objects.create(name=request.POST['name'])
    # y = Interests.objects.create(interest_name=request.POST['interest'])
    # y.users.add(x)


    context = {
        'users' : User.objects.all()
        }
    return render(request, 'mtm_app/results.html', context)
    # return redirect('/showinterest')

def showinterest(request, id):
    # interests = Interests.objects.all()
    # print "looking at all interests"
    # for i in interests:
    #     print i.interest_name
    #     print i.users
    query = User.objects.filter(id=id)
    queryints = query[0].ints.all()
    int_arr = []
    for q in queryints:
        int_arr.append(q.interest_name)
        # print q.interest_name
    
        # print q.interest_name, "* ************"
    # check_query = query[0].values('interest_name')
    context = {
        'yahoo' : int_arr
    }
    return render(request, 'mtm_app/interests.html', context)
