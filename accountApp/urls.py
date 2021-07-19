from django.urls import path
from accountApp.views import helloworld

app_name = 'accountApp'

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
]