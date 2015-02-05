from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['post_header', 'post_content']}),
        ('Date Info', {'fields': ['post_date']})
    ]

    list_display = ('post_header', 'post_date', 'was_published_recently')

    list_filter = ['post_date']

    search_fields = ['post_header']

admin.site.register(Post, PostAdmin)