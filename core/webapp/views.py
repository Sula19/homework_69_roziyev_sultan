from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def action(request, *args, **kwargs):
    data = json.loads(request.body)
    result = 0
    try:
        match request.path:
            case '/add/':
                result += int(data['A']) + int(data['B'])
            case '/subtract/':
                result += int(data['A']) - int(data['B'])
            case '/multiply/':
                result += int(data['A']) * int(data['B'])
            case '/divide/':
                result += int(data['A']) / int(data['B'])
        answer = {
            'answer': result
        }
        return JsonResponse(answer)
    except ZeroDivisionError:
        response = JsonResponse({'error': 'Cannot operate on zero'})
        response.status_code = 400
        return response
    except ValueError:
        response = JsonResponse({'error': 'You entered empty data'})
        response.status_code = 400
        return response
