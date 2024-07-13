# myproject/urls.py
from django.contrib import admin
from django.urls import path
from send_email import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', views.send_email, name='send_email'),
]
