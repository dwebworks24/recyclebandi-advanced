from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from .models import * 
from django.core.serializers import serialize
import pandas as pd
from io import BytesIO
from .forms import UploadFileForm
from .models import Transaction
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    context ={'segment': 'index'}
    try:
        html_template = loader.get_template('home/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('errorpages/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('errorpages/page-500.html')
        return HttpResponse(html_template.render(request))


@login_required(login_url="/login/")
def datatables(request):
    context = {'segment': 'employee'}

    try:
        if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    excel_file = request.FILES['file']
                    df = pd.read_excel(BytesIO(excel_file.read()))

                    for index, row in df.iterrows():
                        Transaction.objects.create(
                            user=request.user,
                            date=row['date'],
                            account_balance=row['account_balance'],
                            withdrawal=row.get('withdrawal', 0),
                            deposit=row.get('deposit', 0),
                            purpose=row['purpose']
                        )
                    return JsonResponse({'status': 'success'}, status=200)
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'Processing error: {str(e)}'}, status=400)
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid form'}, status=400)

        # For GET requests (normal page load)
        html_template = loader.get_template('home/data-tables.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('errorpages/page-404.html')
        return HttpResponse(html_template.render(request))

    except Exception as e:
        html_template = loader.get_template('errorpages/page-500.html')
        return HttpResponse(html_template.render(request))
    
@login_required(login_url="/login/")
def cluster_dashboard(request):
    context ={'segment': 'cluster'}
    try:
        logged_in_user = request.user
      
        html_template = loader.get_template('home/cluster-dashboard.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('errorpages/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('errorpages/page-500.html')
        return HttpResponse(html_template.render(request))
    
    
@login_required(login_url="/login/")
def employee_datatables(request):
    context ={'segment': 'employee'}
    try:
        html_template = loader.get_template('home/data-tables.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('errorpages/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('errorpages/page-500.html')
        return HttpResponse(html_template.render(request))
    
    
@login_required(login_url="/login/")
def password_change(request):
    context ={'segment': 'all'}
    try:
        html_template = loader.get_template('home/password-change.html')
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('errorpages/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('errorpages/page-500.html')
        return HttpResponse(html_template.render(request))
    

# @login_required
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['file']
#             try:
#                 df = pd.read_excel(BytesIO(excel_file.read()))
#                 for index, row in df.iterrows():
#                     Transaction.objects.create(
#                         user=request.user,
#                         date=row['Date'],
#                         account_balance=row['Account Balance'],
#                         withdrawal=row.get('Withdrawal', 0),
#                         deposit=row.get('Deposit', 0),
#                         purpose=row['Transaction Purpose']
#                     )
#                 return redirect('dashboard')
#             except Exception as e:
#                 form.add_error('file', f"File processing error: {str(e)}")
#     else:
#         form = UploadFileForm()
#     return render(request, 'tracker/upload.html', {'form': form})