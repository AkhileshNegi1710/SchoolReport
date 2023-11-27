from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def index(request):

    try:
            send_mail('Hello Student',
                      'Welcome to the Student Email',
                      from_email=settings.EMAIL_HOST_USER, recipient_list=['akhileshnegi1710@gmail.com'], fail_silently=False)
            print("Email sent successfully.")
        # Log success or redirect to a success page
    except Exception as e:
        # Log or print the exception for debugging
        print(f"Error sending email: {e}")
        # Handle the error, redirect to an error page, or return an error response
    return render(request,'studentWelcome/index.html')


