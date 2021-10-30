from django.contrib import admin
from post.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)