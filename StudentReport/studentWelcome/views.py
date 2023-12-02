from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse

from StudentReport import settings


def send_email_view(request):
    # Assume you have a user and items data to pass into the template
    user = request.user  # Fetch the user or use any user instance
    items = ['Item 1', 'Item 2', 'Item 3']  # Sample list of items

    # Render the template with context data
    html_message = render_to_string('studentWelcome/index.html', {'user': user, 'items': items})

    # Send the email
    send_mail('Hello Student',
                      'Welcome to the Student Email',
                      from_email=settings.EMAIL_HOST_USER, recipient_list=['akhileshnegi1710@gmail.com'], fail_silently=False,html_message=html_message
    )

    return HttpResponse('Email sent successfully!')