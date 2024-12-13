from django.shortcuts import render, get_object_or_404
from artistas.models import Artista, Obra
 


# View para a página index_deslogado
def perfil_artista (request, artista_id):
    obras = Obra.objects.filter(artista_id=artista_id)  # Busca todas as obras
    artista = get_object_or_404(Artista, pk=artista_id)
    return render (request, "artistas/perfil_artista.html", {"artista": artista, "obras": obras})

def lista_produtos(request, obra_id):
    
    obra = get_object_or_404(Obra, pk=obra_id)
    artista = obra.artista
    obras = Obra.objects.all()  # Busca todas as obras
    return render(request, 'artistas/obras.html', {'obra': obra, 'artista':artista, 'obras': obras})
