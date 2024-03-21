from django.shortcuts import render

#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello World!")
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            author = formdata['author']
            genre = formdata['genre']
            date = formdata['date']
            ISBN = formdata['ISBN']
            pages = formdata['pages']
            Book.objects.create(title=title, author=author, genre=genre, date=date, ISBN=ISBN, pages=pages)
            return HttpResponseRedirect('/success')
    else:
        form = CreateBookForm()
    return render(request, 'myapp3/createbook.html', {'form': form})


def success(request):
    return render(request, 'myapp3/success.html')
