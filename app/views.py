from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from .models import Item

def input(request):
    return render(request, 'index.html', {})

def input_process(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)

            item = Item()
            item.item_code = data['code']
            item.item_name = data['name']

            item.save()

            return JsonResponse({'message': 'Success'})
        except:
            return JsonResponse({'message': 'Something went wrong'})

def list_items(request):
    context = {
        'item': Item.objects.all()
    }

    return render(request, '', context)