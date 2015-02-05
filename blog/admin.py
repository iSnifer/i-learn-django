from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_header', 'post_content']}),
        ('Date Info', {'fields': ['post_date']})
    ]

admin.site.register(Post, PostAdmin)