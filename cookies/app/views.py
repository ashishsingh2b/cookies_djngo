from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setcookie(request):
    response = render(request,'students/setcookie.html')
    response.set_cookie('lname','jha',expires=datetime.utcnow()+timedelta(days=2))
    response.set_cookie('name','sonam')
    return response


def getcookie(request):
    #name = request.COOKIES['name']
    name =request.COOKIES.get('name',"Guest")
    return render(request,'students/getcookie.html',{'name':name})

def delcookie(request):
    response =render(request,'students/delcookie.html')
    response.delete_cookie('name')
    return response
    
    