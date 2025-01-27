




from django import forms
from .models import Book, Post


class bookform(forms.ModelForm):
    class Meta:
     model = Book
     fields = ('name', 'description',  'price')


class Postform(forms.ModelForm):
    class Meta:
     model = Post
     fields = ('title', 'content',  'created_at')












