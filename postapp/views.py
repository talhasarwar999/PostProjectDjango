from .models import *
from .serializers import *
from rest_framework import viewsets


#Viewsets
class Get_Posts_By_Category(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = CatSerializer



class GetAllPosts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

