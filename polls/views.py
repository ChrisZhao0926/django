from django.http import HttpResponse
from django.core.mail import EmailMessage
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


def index(request):

    return HttpResponse("Hello world!")


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
