from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    if not 'current_user_id' in request.session:
        request.session['current_user_id'] = 0

    query1 = User.uManager.filter(id=request.session['current_user_id'])

    context = {
        'info' : query1
    }

    print'='*100
    print request.session['current_user_id']
    print'='*100

    return render (request, 'pinnit/Pinnit.html', context)

def logreg_page(request):
    return render (request, 'pinnit/logreg_page.html')

def register(request):
    if request.method == "POST":
        result = User.uManager.register(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], confirm=request.POST['confirm'])
        if result[0]:
            request.session['current_user_id'] = result[1].id
            request.session['errors'] = []
            return redirect('/')
        else:
            request.session['errors'] = result[1]
            return redirect('/logreg')
    else:
        return redirect ('/logreg')

def login(request):
    if request.method == "POST":
        result = User.uManager.login(login_username=request.POST['login_username'], login_password=request.POST['login_password'])

        if result[0]:
            request.session['current_user_id'] = result[1][0].id
            request.session['errors'] = []
            return redirect('/')
        else:
            request.session['errors'] = result[1]
            return redirect('/logreg')
    else:
        return redirect ('/logreg')

def sports_page(request):
    if request.session['current_user_id'] != 0:
        query1 = User.uManager.filter(id=request.session['current_user_id'])

        context = {
            'info' : query1
        }
        return render (request, 'pinnit/sports.html', context)
    else:
        return redirect ('/logreg')

def logout(request):
    request.session.pop('current_user_id')
    return redirect('/')
