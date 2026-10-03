"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    PORTA DE ENTRADA DA APLICAÇÃO!
"""
from django.contrib import admin
from django.urls import path, include
# from login.views import index, contact
from django.views.generic.base import TemplateView

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('login.urls')), #/ = traz o subdomínio do app de login
    #path('', include ('register.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    #path('', index), # se eu importar direto a view
    #path('contact', contact), # se eu importar direto a view
]

admin.site.site_header = 'Configurações de Sistema'
admin.site.site_title = 'Criando o sistema dos Capuchinhos'
admin.site.index_title = 'Paz e Bem!'