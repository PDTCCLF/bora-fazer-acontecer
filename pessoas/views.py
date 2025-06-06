from django.shortcuts import render, get_object_or_404, redirect
from .models import Pessoa, Aluno, Voluntario
from .forms import AlunoForm, VoluntarioForm
from django.contrib.auth.models import User


# View para listar todos os alunos
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'pessoas/alunos/lista.html', {'alunos': alunos})

# View para listar todos os voluntários
def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'pessoas/voluntarios/lista.html', {'voluntarios': voluntarios})

# Criar aluno
def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'pessoas/alunos/formulario.html', {'form': form, 'titulo': 'Criar Aluno'})

# Criar voluntário
def criar_voluntario(request):
    if request.method == "POST":
        form = VoluntarioForm(request.POST) # Recebe os dados do formulário
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = User.objects.create_user(
                username=usuario,
                email=email,
                password=senha
            )
            user.is_staff = True   # garante acesso ao painel admin
            user.save()

            voluntario = form.save(commit=False)
            voluntario.usuario = user
            voluntario.save()
            return redirect("lista_voluntarios")
    else:
        form = VoluntarioForm()
    return render(request, 'pessoas/voluntarios/formulario.html', {'form': form, 'titulo': 'Criar Voluntário'})

# Editar aluno
def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'pessoas/alunos/formulario.html', {'form': form, 'titulo': 'Editar Aluno'})

# Editar voluntário
def editar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    form = VoluntarioForm(request.POST or None, instance=voluntario)
    if form.is_valid():
        form.save()
        return redirect('lista_voluntarios')
    return render(request, 'pessoas/voluntarios/formulario.html', {'form': form, 'titulo': 'Editar Voluntário'})

# Deletar aluno
def deletar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'pessoas/alunos/confirma_deletar.html', {'aluno': aluno})

# Deletar voluntário
def deletar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('lista_voluntarios')
    return render(request, 'pessoas/voluntarios/confirma_deletar.html', {'voluntario': voluntario})