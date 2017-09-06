from django.shortcuts import render
from django.http import HttpResponse
import datetime
import textwrap
def index(request):

	time = datetime.datetime.now()
	
	return render(request, 'hello.html', {'hello' : "Hello World. I love Django!", 'time': time})


