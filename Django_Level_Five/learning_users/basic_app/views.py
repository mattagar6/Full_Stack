from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
# djanog built-in imports for logging in/out
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # save the form info directly to the database
            user = user_form.save()
            # this method hashes the inputed Password
            # using the hasher specified in settings.py
            user.set_password(user.password)
            user.save()

            # don't save the new profile info to the database just yet
            profile = profile_form.save(commit = False)
            # this sets up the OneToOne relationship between the built-in user model
            # and the additional attributes we gave (check out models.py)
            profile.user = user

            if 'profile_pic' in request.FILES:
                # request.FILES acts like a dictionary of all uploaded files in the form
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.erros, profile_form.errors)
    else:
        # if it is a GET method, set up the forms
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,
                'basic_app/registration.html',
                context = {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered,
                            })

def user_login(request):

    if request.method == 'POST':
        # if the user has filled in the login information

        # get the information from the html form in basic_app/login.html
        username = request.POST.get('username')
        password = request.POST.get('password')

        # this built in django function automatically authenticates a user for you
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('SOMEONE TRIED TO LOGIN AND FAILED')
            print(f'USERNAME: {username} AND Password: {password}')
            return HttpResponse('INVALID LOGIN DETAILS SUPPLIED ')
    else:
        return render(request, 'basic_app/login.html', context = {})
