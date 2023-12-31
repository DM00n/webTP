import datetime

from app.models import *
from django.core.management.base import BaseCommand

import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными данными'
    Faker.seed(datetime.datetime.now().microsecond)

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Множитель заполнения')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        author_list = Profile.objects.all()
        questions_list = Question.objects.all()
        answers_list = Answer.objects.all()

        for i in range(total):
            user = random.choice(author_list)
            question = random.choice(questions_list)
            answer = random.choice(answers_list)

            LikeQuestion.objects.create(question=question, user=user)
            LikeAnswer.objects.create(answer=answer, user=user)
