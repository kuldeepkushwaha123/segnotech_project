from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def home(request):
    posts = Post.objects.all()
    
    return render(request,'index.html',{'posts':posts})



def post_new(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Blog created successfully')
                return redirect('/')
    
        else:
            form = PostForm()
      
        return render(request,'form.html',{'form':form})


def edit_customer(request,id=None):
    data = Post.objects.get(pk=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render (request,'edit.html',{'form':form})

def delete_customer(request,id=None):
    rec = Post.objects.get(pk=id)
    if request.method == "POST":
        rec.delete()
        return redirect('/')
    return render(request,'delete.html')