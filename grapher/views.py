from django.shortcuts import render,redirect
from .forms import UserCreationForms,UpdateProfile
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib import messages
from .decorators import *
from django.contrib.auth.models import Group
from django.conf import settings
import requests
from django.contrib.auth.decorators import login_required
from .filters_questions import questionfilter

@NoLoggedUser
def register(request):
    graphers = Profile.objects.all()
    form = UserCreationForms()
    if request.method == 'POST' :
        form = UserCreationForms(request.POST)
        if form.is_valid() :
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            resulte = r.json()
            if resulte['success']:
                user = form.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='photographer')
                user.groups.add(group)
                # messages.success(request, username + ' Created Successfully !')
                return redirect('grapher:home')
            else:
                messages.info(
                    request, ' invalid recaptcha please try againe !')
                
    context = {'form':form,'graphers':graphers}
    return render(request,'grp/register.html',context)


def home(request): 
    graphers = Profile.objects.all()
    context = {'graphers':graphers}
    return render(request,'grp/Home.html',context)

# def photographer_detail(request,slug):
#     photographer_detail=Profile.objects.get(slug=slug)

#     return render(request,'grp/look.html',{'photographer_detail':photographer_detail,})

@NoLoggedUser
def log(request):
    graphers = Profile.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            resulte = r.json()
            if resulte['success']:
                login(request, user)
                return redirect('grapher:home')
            else:
                messages.info(
                    request, ' invalid recaptcha please try againe !')
        else :
            messages.info(request, 'there was an error logging you in. please try again.')

    context = {'graphers':graphers}
    return render(request,'grp/login.html',context)

def look(request ,pk):
    graphers = Profile.objects.all()
    grapher = Profile.objects.get(id=pk)
    works = grapher.project_set.all()
    context = {'grapher':grapher,'works':works,'graphers':graphers}
    return render(request,'grp/look.html',context)

def learn(request):
    graphers = Profile.objects.all()
    context = {'graphers':graphers}
    return render(request,'grp/learn.html',context)


def about(request):
    graphers = Profile.objects.all()
    context = {'graphers':graphers}
    return render(request,'grp/about.html',context)


@login_required(login_url='grapher:log')
def call(request ,pk):
    graphers = Profile.objects.all()
    form = inlineformset_factory(Profile,Contact, fields=('phone_number', 'message'), extra=1)
    photographer = Profile.objects.get(id=pk)
    info_contact = form(queryset=Contact.objects.none(), instance=photographer)
    
    if request.method == 'POST':
        info_contact = form(request.POST, instance=photographer)
        if info_contact.is_valid():
            info_contact.save()
            return redirect('grapher:home')

    context = {'info_contact': info_contact,'graphers':graphers}
    return render(request,'grp/callus.html',context)

@login_required(login_url='grapher:log')
def workshops(request):
    graphers = Profile.objects.all()
    context = {'graphers':graphers}
    return render(request,'grp/workshops.html',context)

def pay(request):
    graphers = Profile.objects.all()
    context = {'graphers':graphers}
    return render(request,'grp/pay.html',context)


def allprof(request):
    graphers = Profile.objects.all()
    prof=Profile.objects.all()
    context = {'prof':prof,'graphers':graphers}
    
    return render(request,'grp/allprof.html',context)

def create(request):
    graphers = Profile.objects.all()
    form=Prof_form()
    if request.method=='POST':
        form=Prof_form(request.POST,request.FILES)
        if form.is_valid():
            item=form.save()
            return redirect('grapher:add_my_work',pk=item.id)
    context={'form':form ,'graphers':graphers}
    return render(request,'grp/profile.html',context)

def update_profile(request,pk):
    graphers = Profile.objects.all()
    garpher = Profile.objects.get(id=pk)
    new_grapher = Prof_form(instance=garpher)
    if request.method=='POST':
        new_grapher = Prof_form(request.POST,request.FILES,instance=garpher)
        if new_grapher.is_valid() :
            new_grapher.save()
            return redirect('grapher:home')
        
    context = {'graphers':graphers , 'new_grapher':new_grapher}
    return render(request,'grp/profile.html',context)


def delete_profile(request, pk):
    graphers = Profile.objects.all()
    profile_delete = Profile.objects.get(id=pk)
    user = profile_delete.user
    if request.method == 'POST':
        user.delete()
        profile_delete.delete()
        return redirect('grapher:home')
    context = {'profile_delete': profile_delete ,'graphers':graphers}
    return render(request, 'grp/delete_profile.html', context)

    
def add_img(request,pk):
    graphers = Profile.objects.all()
    
    form = inlineformset_factory(Profile,project,fields=('discription','work'),extra=1)
    grapher = Profile.objects.get(id=pk)
    wrok = form(queryset=project.objects.none(),instance=grapher)
    if request.method == 'POST':
        wrok = form(request.POST, request.FILES, instance=grapher)
        if wrok.is_valid():
            wrok.save()
            return redirect('grapher:home')
    else:
        wrok = form()

    context = {'graphers':graphers , 'wrok': wrok}
    return render(request, 'grp/add_your_work.html',context)

def user_logout(request) :
    logout(request)
    return redirect('grapher:home')


def photographer_profile(request ,pk) :
    graphers = Profile.objects.all()
    grapher = Profile.objects.get(id=pk)
    works = grapher.project_set.all()  
    context = {'grapher':grapher,'works':works , 'graphers':graphers}
    return render(request,'grp/photographer_profile.html',context)


def questions(request):
    query = Contact.objects.all()
    search = questionfilter(request.GET, queryset=query)
    query = search.qs
    num_ques = query.count()
    context = {'query':query,'search':search,'num_ques':num_ques}
    return render(request,'grp/questions.html',context)


    
