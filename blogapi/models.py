from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='likers',blank=True,symmetrical=False)

    def number_of_likes(self):
        if self.likes.count():
            return self.likes.count()
        return 0 
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author_comment = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
      

    def __str__(self):
        return self.title

      
        
