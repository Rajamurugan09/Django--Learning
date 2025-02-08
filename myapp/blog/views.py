from django.shortcuts import render,redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.urls import reverse # type: ignore

# Creating views here.
def index(request):
    blog_title="Latest Posts"
    posts = [
        {'title':'Post 1','content':'Content of Post 1'},
        {'title':'Post 2','content':'Content of Post 2'},
        {'title':'Post 3','content':'Content of Post 3' },
        {'title':'Post 4','content':'Content of Post 4' }, 
    ] 
    
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})
def detail(request,post_id):
    return render(request,'blog/detail.html')
    # return HttpResponse(f"you are ciewing post detail page.and id is {post_id}")


def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("you are at new url")