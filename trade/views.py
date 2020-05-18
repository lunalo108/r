from django.shortcuts import render
from .models import Quote, QuoteTable
from django_tables2 import RequestConfig
    
def quotes_table(request):
    table = QuoteTable(Quote.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'trade/quotes_table.html', {'table': table})

