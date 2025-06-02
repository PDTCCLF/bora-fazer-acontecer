from django.conf import settings
from django.shortcuts import render

# View para a página inicial
def home(request):
    return render(request, "core/home.html", {"debug": settings.DEBUG})
