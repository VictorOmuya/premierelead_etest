from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Questions, Profile
from .sms import send_sms


# Create your views here.
def register(request):
    form = NewUserForm()
    error = ""
    usernames = []
    allusers = User.objects.all()
    usern = allusers.values('username')
    for keys in usern:
        usernames.append(keys['username'])
    
    
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users:login')

        elif request.POST.get('username') in usernames:
            error = 'username already exists'
            print(error)
            
        elif request.POST.get('password') != request.POST.get('password2'):
            error = "problem registering user, enter password again!"
            print(error)
            
        elif len(request.POST.get('password')) < 8:
            error = "password must be at least 8 characters"
        
    
    context={
        'form':form,
        'error' : error
    }
    return render(request,'register.html',context)

def error(request):
    return render(request, 'error.html')

@login_required
def exam(request, id):
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
                
        member = Profile.objects.get(id = id)
        phone_no = member.phone
        
        member.score = score
        member.save()

        score_message = "Your score : %s" %score
        try:
            send_sms(phone_no, score_message)
        except:
            return redirect("users:error")
        
        return redirect("users:success")
    
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

def create_profile(request):
    if request.method =='POST':
        contact_number = request.POST.get('phone')
        user = request.user
        code = request.POST.get('code')
        profile = Profile(user=user,code=code, phone=contact_number, score=0)
        profile.save()
        return redirect('users:profile')
    return render(request,'createprofile.html')

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

