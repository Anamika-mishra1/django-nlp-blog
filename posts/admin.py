from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sentiment', 'get_sentiment_label', 'created_at']
    list_filter = ['sentiment', 'created_at']
