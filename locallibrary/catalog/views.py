# catalog/views.py
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # CHALLENGE: Generate counts for genres and books containing specific words
    # Count genres that contain the word 'fiction' (case-insensitive)
    num_genres_with_word = Genre.objects.filter(name__icontains='drama').count()
    
    # Count books that contain the word 'the' in the title (case-insensitive)
    num_books_with_word = Book.objects.filter(title__icontains='the').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_drama': num_genres_with_word,  # Added variable
        'num_books_with_the': num_books_with_word,   # Added variable
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


from django.views import generic
from .models import Book, Author

class BookListView (generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView (generic.DetailView):
    model = Book

class AuthorListView (generic.ListView):
    model = Author
    paginate_by = 3

class AuthorDetailView (generic.DetailView):
    model = Author