from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def action(request, *args, **kwargs):
    try:
        data = {
            "A": 1234,
            "B": 4567
        }
        match request.path:
            case '/add/':
                result = int(data['A'] + data['B'])
            case '/subtract/':
                result = int(data['A'] - data['B'])
            case '/multiply/':
                result = int(data['A'] * data['B'])
            case '/divide/':
                result = int(data['A'] / data['B'])
        answer = {
            'answer': result
        }
        return JsonResponse(answer)
    except Exception:
        response = JsonResponse({'error': 'Data is not numbers!'})
        response.status_code = 400
        return response
