from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

# for login funcitonality

# from django.core.urlresolvers import reverse -> old version code
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# for login funcitonality


# Create your views here.

def index(request):
    return render(request, 'L5P_App/index.html')
###

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
    
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) # this will call the hashing methods specified in the settings.py file...
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user # setting up 1 to 1 relationship. 

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    
    else: # if the form is not posted

        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }
        
    return render(request, 'L5P_App/registration.html', context)
###

def user_login(request):
    '''
    print(request.GET)
    print("\n")
    print(request.GET['next'])
    '''
    if request.method == "POST":

        username_entered = request.POST.get("username")
        password_entered = request.POST.get("password")

        user = authenticate(username=username_entered, password=password_entered)

        if user:

            if user.is_active:
                login(request, user)

                if(request.POST.get("url_2_fetch")):
                    return HttpResponseRedirect(request.POST.get("url_2_fetch"))
                else:
                    return HttpResponseRedirect(reverse('homepage'))        
                    

            else:
                return HttpResponse("Account not active")
        
        else:

            print("Someone tried to login and failed!")
            print("The details entered are - \n Username: {} and the password: {}".format(username_entered, password_entered))
            return HttpResponse("Invalid login details!!!")

    else:
        if request.GET['next'] != "":
            context = {
                'url_2_fetch' : request.GET["next"],
            }
        else:
            context = {}

        return render(request, "L5P_App/login.html", context)
###

@login_required # this decorator ensures that the user is logged in to access the view
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
###

@login_required
def special_view(request):
    #return HttpResponse("Nice to know, you are logged in!!!")
    context_2_return = {
        "msg":"Nice to know, you are logged in!!!",
        "title": "Speicals View :: Accessible after logging in!"
    }
    return render(request, 'L5P_App/specials.html', context=context_2_return)
###


