from django.shortcuts import render
from datetime import  datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def main (request):
    data = datetime.now()
    return render(
        request,
        'base.html',
        {
            'title': "HOME PAGE",
            "time" : data,
            'home': ' This is Home Page'
        }
    )

def create_account (request):
    if request.method == 'GET':
        return render(
            request,
            'create_account.html',
            {
                'title':'create_account'
            }
        )
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = User.objects.create(
            first_name = first_name ,
            last_name = last_name ,
            email =  email ,
            username = email ,
        )
        obj.set_password(password)
        obj.save()
        return render(
            request,
            'create_account.html',
            {
                'msg': 'Account Created !! '
            }
        )

@login_required
def secure_page(request):
    return render(
        request,
        "secure_page.html",
        {
            'title':'secure page'
        }
    )