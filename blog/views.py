from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Blogcomment
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'Blog/bloghome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=post)
    replies= Blogcomment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
            
    context = {'post':post,'comments':comments,'user': request.user,'replyDict': replyDict}
    return render(request,'Blog/blogpost.html', context)

def postComment(request):
   if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno=="":
            comment = Blogcomment(comment= comment, user=user, post=post)
            comment = Blogcomment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
            return HttpResponse('Your comment has been posted successfully')
        else:
            parent= Blogcomment.objects.get(sno=parentSno)
            comment=Blogcomment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
            return redirect(f"/blog/{post.slug}")



# def index(request):
#     posts = Post.objects.all()
#
#     return render(request,'index.html',{'posts':posts})
#
#
# def home(request):
#
#     return render(request,'home.html')
#
#
# def post_new(request):
#
#         if request.method == 'POST':
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request,'Blog created successfully !')
#                 return redirect('/')
#
#         else:
#             form = PostForm()
#
#         return render(request,'form.html',{'form':form})
#
#
# def postComment(request):
#     if request.method == "POST":
#         pass
#     return redirect('home')
#
#
# def edit_customer(request,slug):
#     data = Post.objects.get(slug=slug)
#     form = PostForm(request.POST or None,request.FILES or None,instance=data)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Blog Updated successfully !')
#         return redirect('/')
#
#     return render (request,'edit.html',{'form':form})
#
# def delete_customer(request,slug):
#     rec = Post.objects.get(slug=slug)
#     if request.method == "POST":
#         rec.delete()
#         messages.success(request,'Blog Deleted successfully !')
#         return redirect('/')
#     return render(request,'delete.html')