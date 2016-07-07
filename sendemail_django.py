from django.core.mail import EmailMessage
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from_addr = "SG-CNBJ-omv-tools-git-G@sonymobile.com"
# from_addr = "chris.zhao@sonymobile.com"
to_addr = 'chris.zhao@sonymobile.com'
cc_list = ['SG-CNBJ-omv-tools-git-G@sonymobile.com']

email = EmailMessage('[Test]django email', 'Hello, just confirm receive mail by DL, please ignore',
                     from_email=from_addr, to=['chris.zhao@sonymobile.com'], cc=cc_list)
email.send()
