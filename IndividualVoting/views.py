from django.shortcuts import render
#Authorship Muhammad Yasin Yahya W1974891
# Create your views here.
from django.http import HttpResponse


#functions used to create the webpages
def vote1(request):
    return render(request,'EngineerVotingSession1.html')

def vote2(request):
    return render(request,'EngineerVotingSession2.html')
def vote3(request):
    return render(request,'EngineerVotingSession3.html')
def vote4(request):
    return render(request,'EngineerVotingSession4.html')
def vote5(request):
    return render(request,'EngineerVotingSession5.html')

def userResponse(request):
    return render(request,'FeedbackResponse.html')

def viewOnly(request):
    return HttpResponse('<h1>welcome to vote viewing</h1>')

def feedbackViews(request):
    if request.method=="POST":
        session = request.POST.get('session')
        emotion = request.POST.get('emotion')
        team = request.POST.get('team')
        print (emotion+" " +session+" "+team)
        return render(request,'FeedbackResponse.html')