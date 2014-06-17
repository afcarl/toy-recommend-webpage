from django.http import HttpResponse
from django.template import RequestContext, loader

def helloworld(request):      
    template = loader.get_template('page_a.html')
    context  = RequestContext(request)
    return HttpResponse(template.render(context)) 
