from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post , Comment
#  Like
from .serializers import PostSerializer , CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser



class PostView(APIView):
    def get(self, request, post_id=None, format=None):
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, post_id, format=None):
         post = get_object_or_404(Post, id=post_id)
         post.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

class CommentView(APIView):
    def get(self, request, post_id=None, comment_id=None, format=None):
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            comments = Comment.objects.filter(post_id=post_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    def post(self, request, post_id=None, format=None):
        post = get_object_or_404(Post, id=post_id)
        data = request.data.copy()
        data['post'] = post.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id=None, comment_id=None, format=None):
        comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)