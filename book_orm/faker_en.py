from django.shortcuts import render

# Create your views here.
from faker import Faker
from datetime import datetime
import random

from book_orm.models import *

# تغییر زبان خروجی فیکر به انگلیسی
fake = Faker('en_US')

# لیست ژانرهای مختلف
genres = ["Fiction", "Science Fiction", "Historical", "Romance", "Children", "Mystery", "Horror", "Philosophical", "Social", "Political"]

# ایجاد 10 نویسنده جدید
for _ in range(10):
    author = Author(
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        joindate=fake.date_between(start_date='-30y', end_date='today'),
        popularity_score=fake.random_int(min=1, max=100)
    )
    author.save()

# ایجاد 10 ناشر جدید
for _ in range(10):
    publisher = Publisher(
        firstname=fake.company(),
        lastname="Publishing",
        joindate=fake.date_between(start_date='-30y', end_date='today'),
        popularity_score=fake.random_int(min=1, max=100)
    )
    publisher.save()

# ایجاد 10 کتاب جدید با روابط تصادفی
for _ in range(10):
    book = Books(
        title=fake.sentence(nb_words=6),
        genre=random.choice(genres),
        price=random.uniform(10, 50),
        published_date=fake.date_between(start_date='-40y', end_date='today'),
        author=random.choice(Author.objects.all()),
        publisher=random.choice(Publisher.objects.all())
    )
    book.save()
