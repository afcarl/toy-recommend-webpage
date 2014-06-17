from django.http import HttpResponse
from django.template import RequestContext, loader
import hashlib

def page_a(request):      
    template = loader.get_template('template.html')
    context  = RequestContext(
        request,
        {
            'title': 'Page A',
            'client_ip_address': get_client_ip(request),
            'user_agent': get_user_agent(request),
        }
    )
    return HttpResponse(template.render(context)) 

def page_b(request):      
    template = loader.get_template('template.html')
    context  = RequestContext(
        request,
        {
            'title': 'Page B',
            'client_ip_address': get_client_ip(request),
            'user_agent': get_user_agent(request),
        }
    )
    return HttpResponse(template.render(context)) 

def page_c(request):      
    template = loader.get_template('template.html')
    context  = RequestContext(
        request,
        {
            'title': 'Page C',
            'client_ip_address': get_client_ip(request),
            'user_agent': get_user_agent(request),
        }
    )
    return HttpResponse(template.render(context)) 


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_agent(request):
    return request.META['HTTP_USER_AGENT']

def generate_user_id_hash(request):
    user_agent = get_user_agent(request)
    ip_address = get_client_ip(request)
    key = ip_address + user_agent
    return hashlib.sha1(key.encode()).hexdigest()
