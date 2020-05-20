from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from quizapp import models
from .models import question,choice
from django.urls import reverse
def addscore(request,question_id):
    score=0
    ques = get_object_or_404(question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        
    except(KeyError,choice.DoesNotExist):
        return render(request,'quizapp/first.html',{
            'ques':ques,
            'error':"you didn't select a choice"
        })

def quizpage(request,question_id):
    ques = get_object_or_404(question, pk=question_id)
    ob1=question.objects.get(pk=question_id)

    
    return render(request,'quizapp/first.html',{'q':ob1,'ques':ques})












def landing(request):
    return render(request, 'quizapp/landing.html')













def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')
def userLogin(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/quizpage')
        else:
            data['error'] = "Username or Password is incorrect"
            res = render(request, 'quizapp/login.html', data)
            return res
    else:
        return render(request, 'quizapp/login.html', data)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'quizapp/signup.html', {'form': form})
