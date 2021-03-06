from random import Random

from django.core.mail import send_mail

from Blog.settings import EMAIL_FROM
from users.models import EmailVerifyReord

def generate_random_str(randomLength=8):
    str=''
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length=len(chars)-1
    random=Random()
    for i in range(randomLength):
        str += chars[random.randint(0,length)]
    return str

def send_emails(email,send_type):
    email_record = EmailVerifyReord()
    email_record.code=generate_random_str(16)
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()



    if send_type == 'register':
        email_title='MEの博客注册激活链接'
        email_content='请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(email_record.code)
        send_mail(email_title,email_content,EMAIL_FROM,[email,])
        
            
    elif send_type == 'forget_pwd':
        email_title='MEの博客密码重置链接'
        email_content='请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(email_record.code)
        send_mail(email_title,email_content,EMAIL_FROM,[email,])
        



