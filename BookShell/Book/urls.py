from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    # path("SignUp/",views.signup,name="signup_page")
]
