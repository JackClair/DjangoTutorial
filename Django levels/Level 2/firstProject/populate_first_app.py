# Configure settings for project
# Need to run this before calling models from application!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')

import django
# Import settings
django.setup()

from faker import Faker
fakeGen = Faker()

import random
from first_app.models import AccessRecord,Webpage,Topic

topics = ['Search','Social','Marketplace','News','Games']
def fetch_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=20):
    for entry in range(N):
        # Since topic is ForeignKey it has to be same for linked records
        top = fetch_topic()

        #Creating fake data
        fake_url = fakeGen.url()
        fake_date = fakeGen.date()
        fake_name = fakeGen.company()

        #Pushing data in database

        #for Webpage
        webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name=fake_name)[0]

        #for AccessRecord
        accessRecord = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    n = int(input('Enter no. of fake entries: '))
    print ('Populating database')
    populate(n)
    print("populated")
