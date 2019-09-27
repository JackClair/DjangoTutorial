# Configure settings for project
# Need to run this before calling models from application!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
# Import settings
django.setup()

from faker import Faker
fakeGen = Faker()

import random
from AppTwo.models import User

def populate(N=20):
    for entry in range(N):
        #Creating fake data
        fake_Fname = fakeGen.first_name()
        fake_Lname = fakeGen.last_name()
        fake_email = fakeGen.email()

        user_detail = User.objects.get_or_create(first_name=fake_Fname, last_name = fake_Lname, email = fake_email)[0]

if __name__ == '__main__':
    n = int(input('Enter no. of fake entries: '))
    print ('Populating database')
    populate(n)
    print("populated")
