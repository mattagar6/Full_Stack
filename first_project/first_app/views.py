from django.shortcuts import render
# import the models we wish to display on the web page
from first_app.models import Topic, WebPage, AccessRecord
from django.http import HttpResponse
# Create your views here.

def index(request):

    # order_by() is a SQL command
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}


    return render(request, 'first_app/index.html', context=date_dict)
