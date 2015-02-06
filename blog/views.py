from django.shortcuts import get_object_or_404, render

from blog.models import Post

def index(request):
    latest_blog_entry = Post.objects.order_by('-post_date')[:5]
    context = {'latest_blog_entry': latest_blog_entry}
    return render(request, 'index.html', context)

def detail(requst, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(requst, 'detail.html', {'post': post})