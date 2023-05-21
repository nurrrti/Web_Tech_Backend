from django.contrib.auth.views import auth_login
from django.urls import path

from bookapp.views import IndexView, SearchView, SearchSuccessView, ArchiveView, \
    ContactsView, ProfileView, ProfileChangeView, LeaveCommentView, CommentLikeView, registerView, BookDetailView

app_name = 'bookapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('book/book/<int:pk>/', BookDetailView.as_view(), name='get_book_by_id'),

    path('book/search/', SearchView.as_view(), name='search_book_by_text'),

    path('book/search/<str:text>', SearchSuccessView.as_view(), name='search_success'),

    path('book/archive/', ArchiveView.as_view(), name='archive'),

    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('profile/change/', ProfileChangeView.as_view(), name='profile_change'),

    # leave commentary
    path('book/book/leavecomment/', LeaveCommentView.as_view(), name='leave_comment'),

    # like commentary
    path('book/book/like/', CommentLikeView.as_view(), name='like_comment'),

    # like article
    path('book/book/like_book/', BookDetailView.as_view(), name='like_book'),


    # AUTH PART
    # localhost:8000/login
    path('', auth_login, name="login"),

    # localhost:8000/register
    path("register/", registerView.as_view(), name="registration"),
]
