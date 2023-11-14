import datetime
import os
import random
import secrets
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Profile

fake = Faker()


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt_rand_string


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными пользователями'
    Faker.seed(datetime.datetime.now().microsecond)

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user = User.objects.create_user(
                username=fake.word() + fake.word() + str(random.randint(1, 10000)),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=generate_alphanum_crypt_string(15))

            image = random.choice(os.listdir("uploads/"))
            Profile.objects.create(user=user, image=image)
