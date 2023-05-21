from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return " ".join((self.author_name, self.author_surname))

    def get_name(self):
        return self.author_name

    def get_surname(self):
        return self.author_surname


class Book(models.Model):
    book_category = models.CharField(max_length=200)

    book_name = models.CharField(max_length=200)

    book_image = models.ImageField(upload_to="book_photos/%Y/%m/%d")

    book_text = models.TextField()

    book_page = models.IntegerField()

    book_date = models.DateTimeField(auto_now_add=True)

    book_rating = models.FloatField(default=0.0)

    book_num_of_views = models.IntegerField(default=0)

    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.book_name

    def increase_view_num(self):
        self.book_num_of_views += 1

    def book_rate(self, newrate):
        self.book_rating += newrate

    def get_book_rating(self):
        return self.book_rating

    def get_book_num_of_views(self):
        return self.book_num_of_views


class CustomUser(AbstractUser):
    user_avatar = models.ImageField(upload_to="user_avatars/", default='NULL')

    def __str__(self) -> str:
        return self.username


class Comment(models.Model):
    comment_text = models.TextField('comment_text')

    comment_date = models.DateTimeField('comment_date', auto_now_add=True)

    comment_rating = models.FloatField(default=0.0)

    comment_on_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    comment_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return " ".join((str(self.id), self.comment_on_book.book_name))

    def rate_comment(self, newrate):
        self.comment_rating += newrate
