from django import forms


class CreateBookForm(forms.Form):
    title = forms.CharField(label='title')
    author = forms.CharField(label='author')
    genre = forms.CharField(label='genre')
    date = forms.DateField(label='date')
    ISBN = forms.CharField(label='ISBN')
    pages = forms.IntegerField(label='pages')