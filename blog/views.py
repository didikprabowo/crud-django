from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from .models  import Post, Category
def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'Blog - Dewi Aaggraini',
        'diskripsi' : 'Blog ',
        'posts' : posts,
    }
    return render(request,'blog/index.html',context)
def detail(request,posts_id):
    posts = Post.objects.get(id=posts_id)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/detail.html', context)
def post(request):
    return render(request, 'blog/post.html')

def create(request):
    print(request.POST)
    title = request.GET['title']
    body = request.GET['body']
    tag  = request.GET['tag']
    data_post = Post(title=title, body=body,category_id =1,tag = tag)
    data_post.save()
    return redirect('/blog')
def edit(request, posts_id):
    posts = Post.objects.get(pk=posts_id)
    context = {
        'posts': posts
    }
    return render(request, 'blog/edit.html', context)
def update(request, id):
    post = Post.objects.get(pk=id)
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.tag  = request.GET['tag']
    post.save()
    return redirect('/blog')
def delete(request, posts_id):
    post = Post.objects.get(pk=posts_id)
    post.delete()
    return redirect('/blog')