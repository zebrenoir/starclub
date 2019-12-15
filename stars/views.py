from django.http import HttpResponse
from django.template import loader
from .models import Actor

def index(request):
    actors = Actor.objects.all()
    template = loader.get_template('stars/index.html')
    context = {
        'actors': actors
    }
    return HttpResponse(template.render(context, request))

def list(request):
    return HttpResponse()