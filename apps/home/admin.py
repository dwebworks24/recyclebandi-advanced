import csv
from django.contrib import admin
from django.http import HttpResponse
# Register your models here.
from .models import *
# Register your models here.
class AdminUserlist(admin.ModelAdmin):
    list_display=('id','username','email')
    list_filter = ['username','email','phone','referal_code']
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"

class AdminTransactionData(admin.ModelAdmin):
    list_display=('id','date','account_balance')
    list_filter = ['date','account_balance']
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"


admin.site.register(Users,AdminUserlist)
admin.site.register(Transaction,AdminTransactionData)
