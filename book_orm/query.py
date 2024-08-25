# from .models import *
from book_orm.models import *


# Exercises:
# 1) Fetch first name and last name of all the new authors ( Authors with popularity_score = 0 are new authors ).
Author.objects.filter(popularity_score =0).values('firstname','lastname')
# <QuerySet [{'firstname': 'آرين', 'lastname': 'اشتری'}, {'firstname': 'حسین', 'lastname': 'شمشیری'}]>

# 2) Fetch first name and popularity score of all authors whose first name starts with A and popularity score is greater than or equal to 8.
Author.objects.filter(firstname__startswith='A',popularity_score__gt = 8).values('firstname','popularity_score')
# <QuerySet [{'firstname': 'Alison', 'popularity_score': 42}]>

# 3) Fetch first name of all the authors with aa case insensitive in their first name.
Author.objects.filter(firstname__contains = 'mo').values('firstname','popularity_score')
# <QuerySet [{'firstname': 'Timothy', 'popularity_score': 3}, {'firstname': 'Timothy', 'popularity_score': 44}]>

# 4) Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25].


5) Fetch list of all the publishers who joined after or in September 2012, output list should only
contain first name and join date of publisher. Order by join date.
6) Add new users in followers of the author with pk = 1.
7) Remove one user from the followers of the author with pk = 1.
8) Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing
Author.objects manager )
9) Retrieve all authors who did not join in 2012.
10) Retrieve Oldest author, Newest author, Average popularity score of authors, sum of price of all
books in database.
11) Retrieve all authors who have no recommender, recommended by field is null.
12)
Maximum popularity score of publisher among all the publishers who published a book for the
author with pk = 1. (Reverse Foreign Key hop)
13) Count the number of authors who have written a book which contains the phrase ‘ab’ case
insensitive.
14) Total price of books written by author with primary key = 1. ( Aggregation over related model ),
oldest book written by author with pk = 1, latest book written by author with pk = 1.
15) Among the publishers in the Publishers table what is the oldest book any publisher has
published.