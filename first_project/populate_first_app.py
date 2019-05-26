import os
# configures the settings for the project -> do this before manipulating models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


# FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, WebPage, Topic
from faker import Faker

# fakegen is an instance of the Faker class
fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    # t is assigned to the model instance created by get_or_create
    # check django doc for more info on get_or_create
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]

    t.save()
    return t

def populate(N = 5):

    for entry in range(N):
        # get the topic for the entry -> this will be used as a ForeignKey in webpg object
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new WebPage entry -> this will be used as a ForeignKey in acc_rec object
        webpg = WebPage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create a fake AccessRecord for that WebPage
        acc_rec = AccessRecord.objects.get_or_create(name  = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(10)
    print('populating complete!')
