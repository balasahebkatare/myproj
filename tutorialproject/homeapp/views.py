from django.shortcuts import render
from homeapp.forms import FeedbackForm
# Create your views here.

def home_view(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    form = FeedbackForm()
    return render(request,'homeapp/home.html',{'form':form})
