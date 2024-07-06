from django.shortcuts import render, get_object_or_404
from . import models


# posts = [
#     {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
#     {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'},
#     {'id': 3, 'title': 'Third Post', 'content': 'This is the third post.'},
# ]

posts = models.Posts.objects.all()

def post_list(request):
    context = {'posts': posts}
    return render(request, 'Blog/post_list.html', context)

def post_detail(request, id):

    # When post is present in views.py
    # post = next((post for post in posts if post['id'] == id), None)
    # context = {'post': post}
    # return render(request, 'Blog/post_detail.html', context)


    # Method-1 To get a post from models and display it.
    # context = {'post': posts[id-1]}
    # return render(request, 'Blog/post_detail.html', context)


    # Method-2 To get a post from models and display it.
    post = get_object_or_404(posts,id=id)
    context = {'post': post}
    return render(request, 'Blog/post_detail.html', context)





