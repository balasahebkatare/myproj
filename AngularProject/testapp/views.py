from django.shortcuts import render
from django.views.generic import TemplateView
from testapp.forms import Educational
from testapp.forms import Electronics
# Create your views here.

def educational(request):
    if request.method=="POST":
        form = Educational(request.POST)
        form.save()
        form=Educational()
        return render(request,'testapp/educational.html',{'form':form})

    form=Educational()
    return render(request,'testapp/educational.html',{'form':form})


def electronics(request):
    if request.method=="POST":
        form = Electronics(request.POST)
        form.save()
        form=Electronics()
        return render(request,'testapp/educational.html',{'form':form})

    form =Electronics()
    return render(request,'testapp/electronics.html',{"form":form})

class HomeView(TemplateView):
    template_name="testapp/home.html"
