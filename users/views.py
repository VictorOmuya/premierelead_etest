from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from .models import Questions, Profile
from .sms import send_sms
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
            profile_obj = Profile.objects.create(user = user , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')
        
    context={
        'form':form,
    }
    return render(request,'register.html',context)

def error(request):
    return render(request, 'error.html')

def exam(request, id):
    member = Profile.objects.get(id = id)
    
    if member.exam_taken == False:
    
        score = 0
        questions = Questions.objects.all()
        user_answer = ""
        context ={
            'question':questions,
        }
        if request.method == 'POST':
            for q in questions:
                user_answer = request.POST.get(q.question)
                print(user_answer)
                if q.Answer == user_answer:
                    score += 5
                    print(score)
                else:
                    score += 0
                    
            
            phone_no = member.phone
            
            member.score = score
            member.exam_taken = True
            member.save()

            score_message = "Your score : %s" %score
            try:
                print(score_message)
                #send_sms(phone_no, score_message)
            except:
                return redirect("users:error")
            
            return redirect("users:success")
    else:
        return redirect("users:taken")
            
    
    return render(request, "exam.html", context)

def sendscore(request):
    member = Profile.objects.get(id = id)
    if request.method == 'POST':  
            phone_no = member.phone
        
    
    return render(request, "exam.html")

@login_required
def profile(request):
    return render(request,'profile.html')

def success(request):
    return render(request,'success.html')

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


def newexam(request, id):
    obj = Questions.objects.all()
    page_n = request.GET.get('page', 1)
    p = Paginator(obj, 1)
    
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
        
    context = {
        'page' : page
    }
    
    if request.method == 'POST':
        for q in obj:
            user_answer = request.POST.get(q.question)
            print(user_answer)
            if q.Answer == user_answer:
                score += 5
                print(score)
            else:
                score += 0
    
    return render(request, 'newexam.html', context)


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
