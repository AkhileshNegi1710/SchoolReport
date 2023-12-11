from django.shortcuts import render,redirect
from .forms import contactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    if request.method == 'POST':
        form = contactForm(request.POST)


        if form.is_valid():
            # cleaned_data remove malicious emails
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('studentWelcome/sendEmail.html',{
                'name':name,
                'email':email,
                'content':content
            })

            send_mail('Test Email','Hello','akhilesh7579@gmail.com',[email],html_message=html)
            return redirect('index')
    else:
        form = contactForm()
    return render(request, 'studentWelcome/index.html',{
        'form':form
    })

