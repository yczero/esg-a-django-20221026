from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):

    post_qs = Post.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {
        'post_list' : post_qs, } )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # 값 그자체 keyword??
    return render(request, 'blog/single_post_page.html',{ 'post' : post ,})
    