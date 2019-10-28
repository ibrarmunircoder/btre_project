from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method == 'POST':
        #Get user data
        first_name = request.POST.get('first_name')
        lasst_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        #check if password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, ('This username already exists.'))
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, ('This email is being used.'))
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=lasst_name)
                #Login After registeration
                # login(request, user)
                # messages.success(request, ('You are successfully logged in.'))   
                # return redirect('pages:index')      
                user.save()
                messages.success(request, ("You are now registered and can login"))
                return redirect('accounts:login')      
        else:
            messages.error(request, ("Password doesn't match."))
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now logged in."))
            return redirect('accounts:dashboard')
        else:
            messages.error(request, ('Invalid {Username} and {password}'.format(username,password)))
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, ('You are logged out'))
        return redirect('pages:index')

    return redirect('pages:index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'user_contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)