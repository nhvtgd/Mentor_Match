from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
#import django.template.RequestContext
from models import *
from forms import *
from hack_day_project import *

def home(request):
    return render_to_response('home.html', {"request_user":request.user})

# Django handling the HTTP request.
def match(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    # Get all the people objects in the data base. candidates is an Array
    mentors = list(CustomUser.objects.filter(mentor=True))
    mentee = CustomUser.objects.get(id=request.user.id)

    # Pass all people to the matching algorithm. Get the best match
    candidateList = MatchingPool(mentors,mentee).match_list()

    print type(candidateList)
    candidateArray = []
    for c in candidateList:
        candidateArray.append(CustomUser.objects.get(name=c))

    #Pass the best match to the html template and render it to the user
    return render_to_response('match.html', {'request_user':request.user, 'candidateArray':candidateArray})


# Insert Tran's Matching algorithm here:
def matcher(candidates):
    #Pass Mentor list and Mentee list
    
    
    return candidates[0]

def signup(request):
    if request.method == 'POST':
        form = Example_Person_Form(request.POST)
        if form.is_valid():
            new_user = form.save()
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user)
            #return render_to_response()
            return HttpResponseRedirect("/profile")
    else:
        form = Example_Person_Form()

    return render_to_response('signup.html', {'form': form, "request_user":request.user,}, context_instance=RequestContext(request))

def profile(request):
    if request.user.is_authenticated():
        currentUser = CustomUser.objects.get(id=request.user.id)
        return render_to_response('user_profile.html', {
            'request_user':request.user,
            'currentUser':currentUser,
            })
    else:
        return signup(request)

def users(request):
    return render_to_response('user_base.html', {
        'request_user':request.user,
        })

def display_user(request, alias):
    currentUser = CustomUser.objects.get(username=alias)
    return render_to_response('user_display.html', {
        'request_user':request.user,
        'currentUser':currentUser,
        })

def user_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        try:
            user = CustomUser.objects.get(name=q)
            return HttpResponseRedirect("/users/" + user.username)
        except CustomUser.DoesNotExist:
            return HttpResponse("Sorry. There is no user named: " + q)
    print "User_search error"
    return HttpResponse("Sorry. There is no user named: " + q)

def user_edit(request):
    if request.method == 'POST':
        form = Example_Person_Form(request.POST, instance=CustomUser.objects.get(id=request.user.id))
        if form.is_valid():
            new_user = form.save()
            #return render_to_response()
            return HttpResponseRedirect("/profile")
        return render_to_response('user_edit.html', {'form': form, "request_user":request.user,}, context_instance=RequestContext(request))
    else:
        form = Example_Person_Form(instance=CustomUser.objects.get(id=request.user.id))
        return render_to_response('user_edit.html', {'form': form, "request_user":request.user,}, context_instance=RequestContext(request))

def logoutUser(request):
    if (request.user.is_authenticated()):
        logout(request)
    return HttpResponseRedirect("/")

def loginUser(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['alias'], password=cd['password'])

            #Authenticate user
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/profile")
        
        #Get user and send to profile page
        #currentUser = CustomUser.objects.filter(username=form['alias'])
        #return render_to_response('user_profile.html', {
        #    'request_user':request.user,
        #    'currentUser':currentUser,
        #    })
    else:
        form = Login()
    return render_to_response('user_login.html', {
        'request_user':request.user,
        'form':form,
        }, context_instance=RequestContext(request))

def add_mentor(request, alias):
    user = CustomUser.objects.get(id=request.user.id)
    mentor = CustomUser.objects.get(username=alias)

    user.mentors.add(mentor)
    mentor.mentees.add(user)
    
    mentor.numMentees = len(mentor.mentees.all())
    mentor.numMentors = len(mentor.mentors.all())
    user.numMentors = len(user.mentors.all())
    user.numMentees = len(user.mentees.all())

    user.save()
    mentor.save()

    return HttpResponseRedirect("/profile")
    
