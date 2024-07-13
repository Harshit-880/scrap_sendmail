# myapp/views.py
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings

def send_email(request):
    subject = 'Python (Selenium) Assignment - Your Name'
    message = 'Please find the attached screenshot of the confirmation page.'
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['bansalnaman44@gmail.com'],
        # cc=['hr@themedius.ai'],
    )
    # email.attach_file('confirmation_page.png')
    email.send()
    return render(request, 'send_email/reh.html')
