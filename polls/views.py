from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
import os
from .forms import NameForm, AddForm
from django.shortcuts import render
from user import get_tester

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


def index(request):

    return render(request, 'polls/add.html')


def sendmail():
    # from_addr = "SG-CNBJ-omv-tools-git-G@sonymobile.com"
    from_addr = "chris.zhao@sonymobile.com"
    to_addr = ['chris.zhao@sonymobile.com']
    # cc_list = ['SG-CNBJ-omv-tools-git-G@sonymobile.com']
    cc_list = []
    email = EmailMessage('[Test]django email', 'Hello, just confirm receive mail by DL, please ignore',
                         from_email=from_addr, to=to_addr, cc=cc_list)
    email.send()
    return HttpResponse('sending')


def check_request(request):
    my_path = request.path
    return HttpResponse(my_path)


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #return HttpResponseRedirect('/thanks/')
            return HttpResponse(form.cleaned_data.get('your_name'))
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a1 = int(a)
    b1 = int(b)
    return HttpResponse(str(a1+b1))


def add_form(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = AddForm()
    return render(request, 'polls/add_post.html', {'form': form})


def get_user(request):
    get_tester()
    return HttpResponse('ok')

