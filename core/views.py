from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# View para a página inicial
def home(request):
    return render(request, "core/home.html", {"debug": settings.DEBUG})
