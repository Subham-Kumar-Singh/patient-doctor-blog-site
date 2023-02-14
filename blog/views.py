from django.shortcuts import render, HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def blogHome(request):
    return render(request, 'blog/blogHome.html')


@login_required(login_url='login')
def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')
