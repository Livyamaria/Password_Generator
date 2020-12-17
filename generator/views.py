from django.shortcuts import render

import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def About(request):
    return render(request,'generator/About.html')
def password(request):


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ]

    if request.GET.get('special'):
        letters.extend(list('!#$%&()*+'))
    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    length =int(request.GET.get('length',12))
    thepassword = ''
    for i in range(length):
        thepassword+=random.choice(letters)


    return render(request,'generator/password.html',{'password':thepassword})
