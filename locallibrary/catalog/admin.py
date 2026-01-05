# from django.contrib import admin
# from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)


# catalog/admin.py
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# ---- Author Admin ----
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Show these columns in the list view
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    
    # Order fields in the edit form (dates side-by-side)
    fields = ['first_name' , 'last_name', ('date_of_birth', 'date_of_death')]


# ---- Book Admin ----
# First, we need a helper method to show genres nicely in the list
# This method MUST be added to the Book model (see Step 2 below)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author',)           # Filter sidebar by author
    search_fields = ('title',)          # Search by book title
    inlines = [BooksInstanceInline]

# ---- BookInstance Admin ----
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # These are the ONLY fields that exist right now
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')   # Very useful filters
    search_fields = ('id',)

    # Group fields in the edit/add form
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# ---- Simple registration for Genre and Language ----
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass