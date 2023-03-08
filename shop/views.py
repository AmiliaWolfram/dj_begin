from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Item, Purchase


def list_item(request):
    last_item_list = Item.objects.all()
    context = {
        'items': last_item_list,
    }
    return render(request, 'list_item.html', context)


def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'detail_item.html', {'item': item})
