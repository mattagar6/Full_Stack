from django.shortcuts import render
# Create your views here.
from AppTwo.models import User
from AppTwo.forms import myForm

def index(request):

    return render(request, 'AppTwo/index.html')

def show_all_users(request):

    user_list = User.objects.all()

    user_dict = {
            'all_users':user_list,
    }

    return render(request, 'AppTwo/users.html', context = user_dict)

def sign_up(request):

    form = myForm()

    if request.method == 'POST':
        form = myForm(request.POST)

        if form.is_valid():
            print('form is valid')
            form.save()
            print('form has been saved')
            # go to the page that shows all the users once you have submitted the form to create a new user
            return show_all_users(request)

    return render(request, 'AppTwo/sign_up_form.html', context = {'form':form})
