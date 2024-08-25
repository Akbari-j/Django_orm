# from .models import *
from book_orm.models import *

a = Books.objects.all()
print(a)