from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, JsonResponse
import json
from .models import Item

def input(request):
    return render(request, '', {})

def input_process(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            item = Item()
            item.item_code = data['item_code']
            item.item_name = data['item_name']

            item.save()

            return JsonResponse({'message': 'Success'})
        except:
            return JsonResponse({'message': 'Something went wrong'})

def list_items(request):
    context = {
        'item': Item.objects.all()
    }

    return render(request, '', context)