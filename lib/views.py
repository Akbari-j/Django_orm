from django.shortcuts import render, get_object_or_404, redirect

from lib.forms import Create_Form
from lib.models import Book


# Create your views here.
def home(request):
    return render(request, 'home.html', {'all_books': Book.objects.all()})


def details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'details.html', {'b': book})


def book_list(request):
    pass


def book_create(request):
    if request.method == 'POST':
        form = Create_Form(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("details", pk=book.pk)
    else:
        return render(request, "create.html", {'form': Create_Form})


def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = Create_Form(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("details", pk=book.pk)
    else:
        form = Create_Form(instance=book)
        return render(request, "create.html", {'form': form})


#
# def delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#
#     if request.method == 'POST':
#         book.delete()
#         return redirect("home")
#     else:
#         book = get_object_or_404(Book, pk=pk)
#         form = Create_Form(instance=book)
#         return render(request, 'confirm_delete.html', {'book': book})

def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect("home")
    else:
        book = get_object_or_404(Book, pk=pk)
        form = Create_Form(instance=book)
        return render(request, 'confirm_delete.html', {'book': book})
