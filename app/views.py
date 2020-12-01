from django.shortcuts import render, HttpResponse
import json

def input(request):
    return render(request, '', {})

def input_process(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            