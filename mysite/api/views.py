from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
# from rest_framework.views import APIView    <--- method to add a custom API (timestamp 24mins)


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    Lookup_field = "pk"
