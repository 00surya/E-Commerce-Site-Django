from django.shortcuts import render
from  django.http import HttpResponse
from .models import Blogpost
def index(request):
    blogposts = Blogpost.objects.all()
    
    
    return render(request,"blog/index.html",{'blogpost':blogposts})

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0] #bcz ye ek string return krega so uske liye apn ko 0 likna podata hai. 
    print(post)
    return render(request,"blog/blogpost.html",{'post':post})


