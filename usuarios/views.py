from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Interesse, Perfil
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from artistas.models import Obra

@csrf_exempt
def cadastro(request):
    # Recuperando todos os interesses disponíveis
    interesses_possiveis = Interesse.objects.all()

    if request.method == 'POST':
        # Coletando os dados do formulário
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        profile_picture = request.FILES.get('profile_picture')
        interesses = request.POST.getlist('interests')  # Coletando os interesses selecionados
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_artist = request.POST.get('is_artist')
        biography = request.POST.get('biography') if is_artist == 'sim' else ''

        # Validação simples
        if password1 != password2:
            return HttpResponse("As senhas não coincidem.", status=400)


        try:
            # Criando o usuário
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            # Criando o perfil do usuário
            perfil = Perfil.objects.create(user=user, data_nascimento=datetime.strptime(birth_date, '%Y-%m-%d'))
            perfil.profile_picture = profile_picture
            perfil.save()

            # Associando os interesses selecionados ao perfil
            for interesse_id in interesses:
                interesse = Interesse.objects.get(id=interesse_id)
                perfil.interesses.add(interesse)

            # Se o usuário é artista, adiciona a biografia
            if is_artist == 'sim':
                perfil.biography = biography
                perfil.save()

            # Logando o usuário após o cadastro
            login(request, user)

            return redirect('/common/indexLogado')  # Redireciona para a página principal após o cadastro

        except ValidationError as e:
            return HttpResponse(str(e), status=400)
    
    # Renderizando o template com a lista de interesses
    return render(request, 'usuarios/cadastro.html', {'interesses_possiveis': interesses_possiveis})

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificando se o usuário existe e se a senha está correta
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se o usuário for encontrado e a senha estiver correta, loga o usuário
            login(request, user)
            messages.success(request, "Login bem-sucedido!")
            return redirect('/common/indexLogado')   # Redireciona para a página inicial ou outra página desejada
        else:
            # Se o login falhar, mostra uma mensagem de erro
            messages.error(request, "Nome de usuário ou senha incorretos.")
            return redirect('/usuarios/cadastro')  # Redireciona de volta para o formulário de login

    # Se for uma requisição GET, renderiza o formulário de login


def perfil_usuario(request, usuario_id):
    obras = Obra.objects.all()  # Busca todas as obras
    usuario = get_object_or_404(Perfil, user__id=usuario_id)
    return render(request, "usuarios/perfil_usuario.html", {"usuario": usuario, "obras": obras})
    
    
