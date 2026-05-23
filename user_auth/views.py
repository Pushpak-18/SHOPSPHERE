from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        a = request.POST['fname']
        b = request.POST['lname']
        c = request.POST['email']
        d = request.POST['username']
        e = request.POST['password']
        print(a, b, c, d, e)
        try:
            u = User.objects.get(username=d)
            return render(request, 'register.html', {'error': 'Username already exists'})
        except:
            u = User.objects.create(
                first_name=a,
                last_name=b,
                email=c,
                username=d,
            )
            u.set_password(e)
            u.save()
            return redirect('login_')   # redirect to login after successful register
    return render(request, 'register.html')


def login_(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
        print(a, b)
        u = authenticate(username=a, password=b)
        print(u)
        if u:
            login(request, u)
            return redirect('home')
        else:
            return render(request, 'login_.html', {'error': 'Invalid username or password'})
    return render(request, 'login_.html')


@login_required(login_url='login_')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login_')
def logout_(request):
    logout(request)           # actually log the user out
    return redirect('login_')


@login_required(login_url='login_')
def reset_password(request):
    
    if request.method == 'POST':
        if 'old_pass' in request.POST:
            oldpass = request.POST['old_pass']
            u = authenticate(username=request.user.username, password=oldpass)
            if u:
                return render(request, 'reset_password.html', {'new_pass': True})
            else:
                return render(request, 'reset_password.html', {'error': 'Old password is wrong'})

        if 'new_pass' in request.POST:
            newpass = request.POST['new_pass']
            u = request.user
            if u.check_password(newpass):
                return render(request, 'reset_password.html', {'error': 'New password cannot be same as old password'})
            u.set_password(newpass)
            u.save()
            return redirect('logout_')

    return render(request, 'reset_password.html')


def forgot_pass(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        try:
            u = User.objects.get(username=username)
            print(u)
            request.session['fp_user'] = username
            return redirect('new_password')
        except:
            return render(request, 'forgot_pass.html', {'error': 'Username does not exist'})
    return render(request, 'forgot_pass.html')


def update_profile(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        u = request.user
        u.first_name = fname
        u.last_name = lname
        u.email = email
        u.save()
        return redirect('profile')
    return render(request, 'update_profile.html')
