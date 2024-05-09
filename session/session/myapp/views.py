from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session ['name'] = 'Ashish'
    request.session ['lname'] = 'Singh'
    return render(request,'students/setsession.html')

def getsession(request):
    name = request.session.get('name',default='Guest')
    lname= request.session.get('lname',default='Guest')
    return render(request,'students/getsession.html',{'name':name,'lname':lname})

def delsession(request):
    if 'name'and 'lname' in request.session:
        del request.session['name']
    if 'lname' in request.session:  # Use another 'if' instead of 'and'
        del request.session['lname']
    return render(request, 'students/delsession.html')
