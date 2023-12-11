from . import views
from django.urls import path
from studentWelcome.views import sending_emails
urlpatterns = [
    path("", views.sending_emails)
]
