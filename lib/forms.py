from django import forms
from lib.models import *


class Create_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
