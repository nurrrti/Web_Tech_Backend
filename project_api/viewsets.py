from .views import *

book_list = APIBookViewSet.as_view({'get': 'list', 'post': 'create'})
book_details = APIBookViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})


author_list = APIAuthorsViewSet.as_view({'get': 'list', 'post': 'create'})
author_details = APIAuthorsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

users_list = APICustomUsersViewSet.as_view({'get': 'list', 'post': 'create'})
user_details = APICustomUsersViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

comments_list = APICommentsViewSet.as_view({'get': 'list', 'post': 'create'})
comment_details = APICommentsViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
