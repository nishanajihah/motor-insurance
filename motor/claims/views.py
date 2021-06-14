from django.forms import ModelForm
# from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserInformation, Vehicle, Loss, Document
from django.contrib.auth import authenticate

class UserForm(ModelForm):
    class Meta:
        model = UserInformation
        exclude = ['status']
        # fields = "__all__"

# class VehicleForm(ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = "__all__"

# class LossForm(ModelForm):
#     class Meta:
#         model = Loss
#         fields = "__all__"

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['docFile', 'photo', ]
    
# Calling all data in model (Accessing)
def index(request):
    return render(request, "claims/home.html", {
        "info": UserInformation.objects.all()
    })

def form(request):

    if request.method == "POST":
        document = DocumentForm(request.POST, request.FILES)

        # name = request.POST["name"]
        # email = request.POST["email"]
        # mobile = request.POST["mobile"]

        # form = authenticate(request, name=name, email=email, mobile=mobile)

        if form.is_valid():
            form = document.save()
            # return redirect('claims/home.html')

        # if form:
        #     form(request, UserInformation)
            return render (request, "claims/home.html", {
                "message": "Submit Successful"
        }) 
        else:
            form = DocumentForm()
            return render (request, "claims/home.html", {
                "message": "Error: Submit Went Wrong"
        })

    return render (request, "claims/home.html")

# def doc_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('claims/home.html')
#     else:
#         form = DocumentForm()
#     return render(request, 'claims/home.html', {
#         'form': form
#     })



    
   

    