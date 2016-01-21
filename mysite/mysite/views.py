from django.http import HttpResponse

def hello(request): 
   return HttpResponse("Hella wurrl!!!")

def home_view(request):
   return HttpResponse("This is home.")
