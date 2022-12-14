from django.shortcuts import render, redirect
from users.models import Profile
from .models import Questions
from .sms import send_sms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def error(request):
    return render(request, 'error.html')

@login_required
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
                return redirect("exam:error")
            
            return redirect("exam:success")
    else:
        return redirect("users:taken")
    
    return render(request, "exam.html", context)


def sendscore(request):
    member = Profile.objects.get(id = id)
    if request.method == 'POST':  
            phone_no = member.phone
        
    return render(request, "exam.html")

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

def success(request):
    return render(request,'success.html')

@login_required
def instruct(request):
    return render(request, 'instruction.html')