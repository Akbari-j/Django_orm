
from django.shortcuts import render

# Create your views here.
from faker import Faker
from datetime import datetime
import random

from book_orm.models import *

fake = Faker('fa_IR')

# لیست ژانرهای مختلف
genres = ["داستانی", "علمی تخیلی", "تاریخی", "عاشقانه", "کودک", "معمایی", "ترسناک", "فلسفی", "اجتماعی", "سیاسی"]

# ایجاد 10 نویسنده جدید
for _ in range(10):
    author = Author(
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        joindate=fake.date_between_dates(date_start=datetime(2000, 1, 1)),
        popularity_score=fake.random_int(min=1, max=100)
    )
    author.save()

# ایجاد 10 ناشر جدید
for _ in range(10):
    publisher = Publisher(
        firstname=fake.company(),
        lastname="انتشارات",
        joindate=fake.date_between_dates(date_start=datetime(1990, 1, 1)),
        popularity_score=fake.random_int(min=1, max=100)
    )
    publisher.save()

# ایجاد 10 کتاب جدید با روابط تصادفی
for _ in range(10):
    book = Books(
        title=fake.sentence(nb_words=6),
        genre=random.choice(genres),
        price=random.uniform(10, 50),
        published_date=fake.date_between_dates(date_start=datetime(1980, 1, 1)),
        author=random.choice(Author.objects.all()),
        publisher=random.choice(Publisher.objects.all())
    )
    book.save()  # اصلاح شده
