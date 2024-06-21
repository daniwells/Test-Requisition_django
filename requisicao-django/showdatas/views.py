from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_datas(request):
    if request.method == 'POST':
        # Processar a requisição POST aqui
        data = request.POST  # Ou request.body para dados JSON
        return JsonResponse({'message': 'Requisição POST bem-sucedida!'})

    return JsonResponse({'message': 'Essa url só aceita requisições POST'}, status=405)

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})