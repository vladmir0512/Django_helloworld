from django.http import HttpResponse



def homePageView(req):
	return HttpResponse('Hello world!')
