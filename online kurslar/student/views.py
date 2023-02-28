from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Courses, Contact, about_user, Category, videos_post, CommentPost
from .forms import Registerfrom
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout



def home_send(request):
    posts = Post.published.all()
    return render(request, 'blog/home.html', {'posts':posts})


def courses_send(request):
    sends = Courses.published.all()
    return render(request, 'blog/courses.html', {'sends':sends})

def Contact_up(request):
    if request.method == "POST":
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(full_name, email, message)
        Contact.objects.create(full_name=full_name, email=email,  message=message)
        return redirect('contact')
    return render(request, 'blog/contact.html')


def about_send(request):
    send_posts = about_user.published.all()
    return render(request, 'blog/about.html', {'send_posts':send_posts})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("parol yoki usernameda xatto bor")
            messages.error(request, 'email foydalanilgan ')
            return redirect('login')
    else:
        return render(request, 'blog/sign.html')





def registertion(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(username)
            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.error(request, 'Bu nom foydalanilgan')
                    print("Bu nom foydalanilgan")
                    return redirect('register')
                elif User.objects.filter(email = email).exists():
                    messages.error(request, 'email foydalanilgan ')
                    print("email foydalanilgan ")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    login(request, user)
                    print("ajoyib re'yhatdan o'tdingiz!!!")
                    messages.success(request, "ajoyib re'yhatdan o'tdingiz!!!")
                    return redirect('home')
            else:
                print("Parollar bir biriga mos emas akan??")
                messages.error(request, 'Parollar bir biriga mos emas akan??')
                return redirect('register')
        else:
            return render(request, 'blog/register.html')
        
        
        
def logout_user(request):
    logout(request)
    messages.success(request, "chiqib ketdingiz acountdan")
    return redirect('home')



class Postlist(ListView):
    queryset = videos_post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'


def category_post(request, slug):
    object_list = videos_post.objects.filter(category__slug = slug)
    cats = Category.objects.get(slug=slug)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:    
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/categorys_post.html", {'posts':posts, 'page':page, 'cats':cats})



def post_detail(request, year, month, day, slug):
    post = get_object_or_404(videos_post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)
    if request.method == "POST":
        comment = request.POST.get("text")
        user = request.user
        if len(comment) != 0:
            CommentPost.objects.create(post = post, author = user, body=comment)
    # form = CommentForm(request.POST)
    kamentiyara = CommentPost.objects.filter(post=post).select_related('author')
    return render(request, 'blog/post_detail.html', {'post':post, 'kamentiyara':kamentiyara})


def page_not_fount(request, exception):
    return render(request, 'blog/proba.html')
