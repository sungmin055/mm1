from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'created_at')
    search_fields = ('title', 'user_id')
    list_filter = ('created_at',)