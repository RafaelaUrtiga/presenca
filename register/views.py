from django.shortcuts import render

from django.shortcuts import render

def index (request):
    print(dir(request))
    print(f"\n User: {request.user}")
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário Logado'
    context = {
        'curso': 'Tela de Login',
        'logado': teste

    }
    return render (request, 'index.html', context)

def contact(request):
    return render (request, 'contact.html')
