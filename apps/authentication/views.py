from django import template
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from  apps.home.models import *
from django.template import loader, TemplateDoesNotExist

# Create your views here.
@csrf_exempt
def user_login(request):
    context = {'segment': 'index'}

    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successful.',
                    'redirect_url': '/dashboard/'
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid email or password.'
                })

        # Render login page if not POST
        html_template = loader.get_template('accounts/otp-login.html')
        return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render({}, request))

    except Exception as e:
        print("Login Error:", e)  # helpful for debugging
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render({}, request))
    

def sigin(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('accounts/verify-otp.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
 

@login_required
def logout_view(request):
    context ={}
    try:
        logout(request)
        return redirect('/')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))