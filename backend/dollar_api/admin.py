from django.contrib import admin, messages
from dollar_api.models import Dollar
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
import json
import datetime


class JsonImportForm(forms.Form):
    json_upload = forms.FileField(allow_empty_file=False)


@admin.register(Dollar)
class DollarAdmin(admin.ModelAdmin):
    list_display = ['date', 'source', 'value_sell', 'value_buy']

    def get_urls(self):
        urls = super().get_urls()

        new_urls = [
            path('fill-database/', self.upload_json),
        ]
        return new_urls + urls
    
    def upload_json(self, request):

        if request.method == 'POST':
            json_file = request.FILES['json_upload']
            if not json_file.name.endswith('.json'):
                messages.warning(request, 'The file extention is wrong!!!')
                return HttpResponseRedirect(request.path-info)
            json_data = json.loads(json_file.read().decode('utf-8'))
            for obj in json_data:
                date = datetime.date.fromisoformat(obj['date'])
                Dollar.objects.create(date=date, source=obj['source'], value_buy=obj['value_buy'], value_sell=obj['value_sell'])

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = JsonImportForm()
        data =  { "form": form }
        return render(request, 'admin/fill_database_with_file.html', data)