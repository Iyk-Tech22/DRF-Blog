from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Defines the modep to serialize """
    class Meta:
        model = Post
        fields = ("id", "title", "author", "content", "status")
        
