import os
# configures the settings for the project -> do this before manipulating models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()


# FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 10):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        new_user = User.objects.get_or_create(firstName = fake_first_name, lastName = fake_last_name, email = fake_email)

if __name__ == '__main__':
    print('populating script!')
    populate()
    print('populating complete!')
