from django.shortcuts import render
from .models import Book
# from .forms import SignUpForm
# from django.contrib.auth import login,authenticate
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    book=Book.objects.all()
    return render(request,"Book/index.html",{"Book":book})
# def signup(request):
#     if request.method=="POST":
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             return redirect("signup_page")
#     else:
#         form=SignUpForm()
#     return render(request,"Book/signup.html",{"form":form})    



