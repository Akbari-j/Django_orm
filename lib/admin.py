from django.contrib import admin

from lib.models import Book,Author

# Register your models here.

admin.site.register([Book, Author])