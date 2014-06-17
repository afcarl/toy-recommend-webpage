from django.http     import HttpResponse
from django.template import RequestContext, loader
from webapp.models   import AccessHistory
import hashlib


def view_page_a(request):      
    params_dict = {'title': 'page-a'}
    return view_page(request, params_dict)

def view_page_b(request):      
    params_dict = {'title': 'page-b'}
    return view_page(request, params_dict)

def view_page_c(request):      
    params_dict = {'title': 'page-c'}
    return view_page(request, params_dict)

def view_page(request, params_dict):
    template = loader.get_template('template.html')
    params_dict.update(get_basic_parameters(request))
    context  = RequestContext(request, params_dict)
    return HttpResponse(template.render(context)) 

def fetch_user_access_history(request):
    try:
        return AccessHistory.objects.get(key = generate_user_id_hash(request))
    except:
        return AccessHistory(key = generate_user_id_hash(request))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_basic_parameters(request):
    basic_parameters = {
            'client_ip_address' : get_client_ip(request),
            'user_agent'        : get_user_agent(request),
            }
    return basic_parameters 

def get_user_agent(request):
    return request.META['HTTP_USER_AGENT']

def generate_user_id_hash(request):
    user_agent = get_user_agent(request)
    ip_address = get_client_ip(request)
    key = ip_address + user_agent
    return hashlib.sha1(key.encode()).hexdigest()
