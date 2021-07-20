from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from accountApp.models import HelloWorld

# Create your views here.

def helloworld(request):

	if request.method == "POST":

		data = request.POST.get('helloworld_input')

		db = HelloWorld()
		db.text = data
		db.save()

		return HttpResponseRedirect(reverse('accountApp:helloworld'))
	else:
		wholeData = HelloWorld.objects.all()

		return render(request, 'accountApp/helloworld.html', context={'helloworld_output': wholeData})
		# return render(request, 'accountApp/helloworld.html', context={'text': 'GET method!'})
 