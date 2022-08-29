from django.shortcuts import render
from BlogDesign.models import Post
# from django.views.decorators.debug import sensitive_variables
 
# Create your views here.

# @sensitive_variables('allPosts', 'context')
def projects(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts' : allPosts}
    return render(request, "projects.html", context)

# @sensitive_variables('post', 'context')
def BlogPosts(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post' : post
    }
    return render(request, "BlogPosts.html", context)
