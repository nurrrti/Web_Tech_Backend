from .serializers import *
from rest_framework import response, reverse
from rest_framework.views import APIView  # used for APIRoot
from rest_framework import permissions  # used to set permissions on api access
from .permissions import IsStaffOrNot  # custom permission for accessing api
# using ModelViewSet class to include all the HTTP protocol methods in one CBV
from rest_framework import viewsets


class APIBookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.order_by('-book_date')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all editors
class APIAuthorsViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all comments
class APICommentsViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)


# API: CBV for getting all users
class APICustomUsersViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        # if an array of data was passed then set serializer to accept many
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
