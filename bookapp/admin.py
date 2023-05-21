from django.contrib import admin

from bookapp.models import Book, CustomUser, Author, Comment


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields = ('book_name', 'book_text', 'book_author', 'book_image', 'book_page')
    list_display = ('book_name', 'book_author')
    list_filter = ['book_rating', 'book_author']
    search_fields = ['book_text', 'book_name']


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'is_superuser', 'is_staff', 'is_active', 'user_avatar')


admin.site.register(Author)

admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Comment)
