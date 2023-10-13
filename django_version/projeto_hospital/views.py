from django.http import HttpResponse
from django.template import loader
import os
def hello(request):
    return HttpResponse("Olá, Mundo!" + str(os.getcwd()))

def home(request):
    template = loader.get_template('./projeto_hospital/templates/home.html')
    return HttpResponse(template.render())