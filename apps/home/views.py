from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.
# @login_required(login_url="/login/")
def index(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))



def datatables(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/data-tables.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))



# @login_required
# def logout_view(request):
#     context ={}
#     try:
#         logout(request)
#         return redirect('/')
#     except template.TemplateDoesNotExist:
#         html_template = loader.get_template('uifiles/page-404.html')
#         return HttpResponse(html_template.render(request))
#     except:
#         html_template = loader.get_template('uifiles/page-500.html')
#         return HttpResponse(html_template.render(request))
    