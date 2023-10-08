from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """ Handle request list endpoint """
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveDestroyAPIView):
    """ Handle request for Resource Represtation """
    queryset = Post.objects.all()
    serializer_class = PostSerializer