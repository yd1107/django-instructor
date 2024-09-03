from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"
 
class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'