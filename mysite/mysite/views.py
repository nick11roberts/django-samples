from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hella wurrl!!!")

def home_view(request):
    return HttpResponse("This is home.")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
