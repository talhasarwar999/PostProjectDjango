from rest_framework import serializers
from .models import *


#Serialziers of API
class PostCommentSerializer(serializers.ModelSerializer):
    #Model Serializer
    class Meta:
        model = PostComment
        fields = ['id','comment','post']


class PostMediaSerializer(serializers.ModelSerializer):
    # Model Serializer
    class Meta:
        model = PostMedia
        fields = ['id','name','post']


class PostSerializer(serializers.ModelSerializer):
    #Nested Serializers
    comments = PostCommentSerializer(many=True, read_only=True)
    media = PostMediaSerializer(many=True, read_only=True)

    # Model Serializer
    class Meta:
        model = Post
        fields = ['id','title','author','content','status','comments','media']


class CatSerializer(serializers.ModelSerializer):
    # Nested Serializer
    categoryname = PostSerializer(many=True, read_only=True)
    # Model Serializer
    class Meta:
        model = PostCategory
        fields = ['id','category','categoryname']