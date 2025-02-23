from itertools import chain
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Followers, LikePost, Post, Profile
from django.db.models import Q
from datetime import datetime

def signup(request):
    try:
        if request.method == 'POST':
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            my_user = User.objects.create_user(fnm, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request, my_user)
                return redirect('/')
            return redirect('/login')
    except:
        invalid = "User already exists"
        return render(request, 'signup.html', {'invalid': invalid})
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/')
        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})
    return render(request, 'loginn.html')

@login_required(login_url='/login')
def logoutt(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def home(request):
    following_users = Followers.objects.filter(follower=request.user.username).values_list('user', flat=True)
    post = Post.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    
    search_query = request.GET.get('search', '')
    if search_query:
        post = post.filter(Q(caption__icontains=search_query) | Q(user__icontains=search_query))
    
    context = {
        'post': post,
        'profile': profile,
        'search_query': search_query,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return redirect('/')

@login_required(login_url='/login')
def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)
        like_filter = LikePost.objects.filter(post_id=id, username=username).first()
        if like_filter is None:
            LikePost.objects.create(post_id=id, username=username)
            post.no_of_likes += 1
        else:
            like_filter.delete()
            post.no_of_likes -= 1
        post.save()
        return redirect('/#' + str(id))

@login_required(login_url='/login')
def explore(request):
    post = Post.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    context = {
        'post': post,
        'profile': profile,
    }
    return render(request, 'explore.html', context)

@login_required(login_url='/login')
def profile(request, id_user):
    user_object = User.objects.get(username=id_user)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=id_user).order_by('-created_at')
    user_post_length = len(user_posts)
    follower = request.user.username
    user = id_user
    follow_unfollow = 'Unfollow' if Followers.objects.filter(follower=follower, user=user).first() else 'Follow'
    user_followers = len(Followers.objects.filter(user=id_user))
    user_following = len(Followers.objects.filter(follower=id_user))
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'profile': profile,
        'follow_unfollow': follow_unfollow,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    if request.user.username == id_user:
        if request.method == 'POST':
            image = request.FILES.get('image') or user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            return redirect('/profile/' + id_user)
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/profile/' + request.user.username)

@login_required(login_url='/login')
def search_results(request):
    query = request.GET.get('q')

    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)

    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'search_user.html', context)
# def search_results(request):
#     query = request.GET.get('q')
#     users = Profile.objects.filter(user__username__icontains=query)
#     posts = Post.objects.filter(caption__icontains=query)
#     context = {
#         'query': query,
#         'users': users,
#         'posts': posts,
#     }
#     return render(request, 'search_user.html', context)

def home_post(request, id):
    post = Post.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'post': post,
        'profile': profile,
    }
    return render(request, 'main.html', context)

def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
        if Followers.objects.filter(follower=follower, user=user).first():
            Followers.objects.get(follower=follower, user=user).delete()
        else:
            Followers.objects.create(follower=follower, user=user)
        return redirect('/profile/' + user)
    return redirect('/')
