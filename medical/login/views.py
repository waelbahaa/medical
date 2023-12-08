from django.shortcuts import render
from .models import Register
from login.form import RegisterForm

from django. contrib import messages
# Create your views here.
def login_info(request):
    form=RegisterForm(request.POST, request.FILES)
    if request.method=="POST":
       
       if form.is_valid():
            if request.POST.get("password")==request.POST.get("confirmpassword"):
                form.save()
                if request.POST.get("Status")=="1":
                    context={"pic":request.POST.get("Profilepicture"),"firstname":request.POST.get("firstname")}
                    return render(request,"pat.html",{'form' : form})
                else:
                    return render(request,"doc.html",{'form' : form})
            else:
                messages.error(request,"password not matched")
                
    return render(request,"register.html", {'form' : form})