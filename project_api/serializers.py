from cgitb import lookup
from dataclasses import field
from rest_framework import serializers

from bookapp.models import Book, Comment, CustomUser, Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # article_editor = serializers.HyperlinkedRelatedField(many=True,
    #     view_name='pro_api:editor-detail', read_only=True, lookup_field='id')

    # url = serializers.HyperlinkedIdentityField(view_name='article-detail', lookup_field='id')

    class Meta:
        model = Book
        # fields = ['id', 'article_name', 'article_editor',
        #           'article_date', 'article_rating', 'article_num_of_views']
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['article_editor'] = EditorSerializer(read_only=True)
        return super().to_representation(instance)


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='pro_api:user-detail')
    class Meta:
        model = CustomUser
        # fields = ['username', 'user_avatar', 'password']
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # comment_on_article = serializers.HyperlinkedRelatedField(
    #     view_name='pro_api:article-detail', read_only=True)

    # comment_owner = serializers.HyperlinkedRelatedField(
    #     view_name='pro_api:user-detail', read_only=True)

    # url = serializers.HyperlinkedIdentityField(view_name='pro_api:comment-detail')

    class Meta:
        model = Comment
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     self.fields['comment_on_article'] = ArticleSerializer(read_only=True)
    #     self.fields['comment_owner'] = CustomUserSerializer(read_only=True)
    #     return super().to_representation(instance)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='pro_api:editor-detail')
    class Meta:
        model = Author
        fields = '__all__'
