from django.shortcuts import render


posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'},
    {'id': 3, 'title': 'Third Post', 'content': 'This is the third post.'},
]

def post_list(request):
    context = {'posts': posts}
    return render(request, 'Blog/post_list.html', context)

def post_detail(request, id):
    post = next((post for post in posts if post['id'] == id), None)
    context = {'post': post}
    return render(request, 'Blog/post_detail.html', context)


