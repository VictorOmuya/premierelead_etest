from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate,login

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('users:login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj).first()
        

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('users:login')

        user = authenticate(username = username, password = password)
        print(user)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('users:login')
        
        login(request , user)
        return redirect('users:profile')

    return render(request , 'login.html')

def register(request):
    form = NewUserForm()
    
    usernames = []
    allusers = User.objects.all()
    usern = allusers.values('username')
    for keys in usern:
        usernames.append(keys['username'])
    
    if request.method =='POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user_obj = User(username = username , email = email, password=password)
            user_obj.set_password(password)
            #user_obj.save()
            auth_token = str(uuid.uuid4())
            #print('http://127.0.0.1:8000/verify/'+auth_token)
            profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
            profile_obj.save()
            #send_mail_after_registration(email , auth_token)
            return redirect('/token')
        
    context={
        'form':form,
    }
    return render(request,'register.html',context)
            
    
@login_required
def profile(request):
    return render(request,'profile.html')

#def create_profile(request):
#    if request.method =='POST':
#        contact_number = request.POST.get('phone')
#        user = request.user
#        code = request.POST.get('code')
#        
#        member = Profile.objects.get(id = id)       
#        profile = Profile(user=user,code=code, phone=contact_number, score=0)
#        profile.save()
#        return redirect('users:profile')
#    return render(request,'createprofile.html')

def update(request, id):
    member = Profile.objects.get(id = id)
    
    context = {
        'member' : member
    } 
    
    if request.method == 'POST':
        contact_number = request.POST.get('phone')
        code = request.POST.get('code')
        member = Profile.objects.get(id=id)
        member.code = code
        member.phone = contact_number
        member.save() 
        return redirect('users:profile')

    return render(request, 'update.html', context)

def taken(request):
    return render(request, 'taken.html')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    
def regsuccess(request):
    return render(request , 'regsuccess.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('users:login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('users:regsuccess')
        else:
            return redirect('users:error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')
