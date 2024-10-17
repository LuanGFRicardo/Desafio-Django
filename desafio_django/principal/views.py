from django.shortcuts import render
import csv
from django.conf import settings
import os

# Create your views here.

# View para página Home
def home(request):
    return render(request, 'principal/home.html')

# View para a página de inserção da URL da imagem
def image_url(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        return render(request, 'principal/image_url.html', {'image_url': image_url})
    return render(request, 'principal/image_url.html')

# View para exibir a tabela de dados do CSV
def exibir_tabela(request):
    dados = []
    caminho_csv = os.path.join(settings.BASE_DIR, 'alunos.csv')

    # Lê o arquivo CSV
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        leitor_csv = csv.reader(csvfile)
        next(leitor_csv)
        for linha in leitor_csv:
            dados.append({
                'nome': linha[0],
                'idade': linha[1],
                'peso': linha[2],
                'altura': linha[3],
            })

    # Renderiza a tabela com os dados extraídos do CSV
    return render(request, 'principal/exibir_tabela.html', {'dados': dados})