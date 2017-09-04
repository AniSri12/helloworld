from django.shortcuts import render
from django.http import HttpResponse
import datetime
import textwrap
def index(request):

	time = datetime.datetime.now()
	html = textwrap.dedent('''\
		<!DOCTYPE html>
		<html>
			<body> It is now %s. </body> 
			<p> Hello World! Django is Fun! </p> 
		</html>
        ''') % time 
	return HttpResponse(html)


