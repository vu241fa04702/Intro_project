from django.shortcuts import render

# Create your views here.
# http://127.0.0.1:8000/user/message



from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Student App")
def greet(request):
    return HttpResponse("i am your queen")
def get_name(request):
    return HttpResponse("i am your king")
def user_data(request):
    return HttpResponse(
                        "amit : age "
                        "ahgd : chaloo")
def greet_to_user(request,name,age):
    return HttpResponse(f"hii,{name} good morning <br>"
                        f"your age is {age}")