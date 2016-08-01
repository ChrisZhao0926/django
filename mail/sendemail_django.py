from django.core.mail import EmailMessage
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# from_addr = "SG-CNBJ-omv-tools-git-G@sonymobile.com"
from_addr = "DL-CNBJ-FOTA-EMMA-Lab@sonymobile.com"
# from_addr = "chris.zhao@sonymobile.com"
to_addr = 'OMVFOTATest@sonymobile.com'
# cc_list = ['SG-CNBJ-omv-tools-git-G@sonymobile.com']
#cc_list = ['DL-CNBJ-FOTA-EMMA-Lab@sonymobile.com']
#cc_list = ['DL-CNBJ-TCT_EMMA_Coordination@sonymobile.com']
cc_list = ['chris.zhao@sonymobile.com', ]
#cc_list = ('DL-CNBJ-FOTA-EMMA-Lab@sonymobile.com',)


email = EmailMessage('[Test]django email ', 'Hello, just confirm receive mail by DL, please ignore',
                     from_email=from_addr, to=[to_addr], cc=cc_list)
email.send()
