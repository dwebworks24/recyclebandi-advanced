from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
def otp_login(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/otp-login.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    

def sigin(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/sigin.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))