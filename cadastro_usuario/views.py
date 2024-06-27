from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def logar(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        senha = request.POST.get('senha')
        try:
            user = Usuario.objects.get(nickname=nickname,senha=senha)
            request.session['user_id'] = user.nickname
            return redirect('home')
        except Usuario.DoesNotExist:
            messages.error(request, "Login incorreto.")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def home(request):
    if 'user_id' in request.session:
        usuario = Usuario.objects.get(nickname=request.session['user_id'])
        return render(request, 'home.html', {'usuario': usuario})
    else:
        return redirect('login_user')


def create_usuario(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nickname = request.POST.get('nickname')
    novo_usuario.name = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.age = request.POST.get('idade')
    novo_usuario.senha = request.POST.get('senha')

    # Validação básica
    if not (novo_usuario.nickname and novo_usuario.name and novo_usuario.email and
            novo_usuario.age and novo_usuario.senha):
        messages.error(request, "Todos os campos são obrigatórios!")
        return render(request, 'cadastro.html')
    else:
        novo_usuario.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        return render(request, 'cadastro.html')


def update_user(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    usuario = Usuario.objects.get(nickname=request.session['user_id'])

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        senha = request.POST.get('senha')

        if nome:
            usuario.name = nome
        if email:
            usuario.email = email
        if idade:
            usuario.age = idade
        if senha:
            usuario.senha = senha

        usuario.save()
        messages.success(request, "Dados atualizados com sucesso.")
        return redirect('home')

    return render(request, 'update_user.html', {'usuario': usuario})


def delete_user(request):
    if 'user_id' not in request.session:
        return redirect('login_user')

    usuario = Usuario.objects.get(nickname=request.session['user_id'])

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Conta excluída com sucesso.")
        return redirect('login_user')
    
    return render(request, 'confirmar_delete.html', {'usuario': usuario.name})

def read_usuario(request):
    # exibir todos os usuários numa tabela
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # retornar os dados ao usuário
    return render(request, 'usuarios.html', usuarios)

def logout_user(request):
    if request.method == 'POST':
        request.session.flush()  # Limpa todas as chaves da sessão
        return redirect('login_user')
    return render(request, 'index.html')  # Renderiza a página de login caso não seja POST