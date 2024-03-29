import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

import django
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()


def population(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name= fake_first_name, last_name= fake_last_name, email=fake_email)

if __name__=='__main__':
    print('Population start')
    population(20)
    print('population complete')