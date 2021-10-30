from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    keyword = models.CharField(max_length=80)
    thumbnail = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title