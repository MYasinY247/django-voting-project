"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Authorship Muhammad Yasin Yahya W1974891
from django.contrib import admin
from django.urls import path
from IndividualVoting import views as votingViews

#creating url paths, the .yellow represents the defs made in views.py, the orange reps the url path 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('voting1',votingViews.vote1),
    path('voting2',votingViews.vote2),
    path('voting3',votingViews.vote3),
    path('voting4',votingViews.vote4),
    path('voting5',votingViews.vote5),
    path('watch',votingViews.viewOnly),
    path('voting/FeedbackOutcome',votingViews.userResponse),
    path('feedback/',votingViews.feedbackViews, name="feedback")
]
