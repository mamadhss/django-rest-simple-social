from .models import Post,Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    author_comment = serializers.ReadOnlyField(source='author_comment.name')
    class Meta:
        model = Comment
        fields = ['text','author_comment'] 

        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    comments = CommentSerializer(many=True,read_only=True)
    number_of_comments = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        fields = ['author','title','text','comments','number_of_comments','liked_by_req_user','number_of_likes']
           
    def get_number_of_comments(self,obj):
        return Comment.objects.filter(post=obj).count()   

    




