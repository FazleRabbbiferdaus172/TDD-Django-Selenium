from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.


def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()

    return render(request, 'home.html', context={'new_item_text': request.POST.get('item_text', '')})
