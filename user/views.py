from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .forms import UserRegisterForm
from tradexa.common import post_and_product_list
from datetime import datetime
from .models import Post

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard:home')
   
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            form = login(request,user)
            messages.success(request, f' Welcome {email} !!')

            return redirect('user_dashboard:home')

        return render(request, 'login.html', {'login_error':"Email password wrong"})
   
    return render(request, 'login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard:home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            form.save()
            return redirect('user_dashboard:login')
    
    return render(request, 'signup.html')

def index(request):
    if not request.user.is_authenticated:
            return redirect('user_dashboard:login')
    
    data = post_and_product_list(request)
    return render(request, "index.html", data)


def add_list_post(request):
    if not request.user.is_authenticated:
            return redirect('user_dashboard:login')
    
    if request.method == 'POST':
            
        data = request.POST.get('text_post')
        post_text = Post.objects.create(
            text = data,
            user = request.user
        )
        
        data = post_and_product_list(request)
        return render(request, "index.html", data)

    data = post_and_product_list(request)
    return render(request, "index.html",data)


def user_logout(request):
    logout(request)
    return redirect('user_dashboard:login')


def update_user_post(request):
    if not request.user.is_authenticated:
        return redirect('user_dashboard:login')
    
    if request.method == "POST":
        try:
            text_id = request.POST.get('post_id')
            text_value = request.POST.get('text_post')
            
            if text_id and text_value:
                text_data = Post.objects.get(id=text_id)
                text_data.text = text_value
                text_data.updated_at = datetime.now()
                text_data.save()

                data = post_and_product_list(request)
                return render(request, "index.html", data)

        except Exception as e:
            data = post_and_product_list(request)
            return render(request, "index.html", data)
    
    data = post_and_product_list(request)
    return render(request, "index.html", data)
