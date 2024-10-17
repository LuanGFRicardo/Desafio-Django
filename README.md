Desafio Django - Exibição de Imagem e Tabela de CSV

Este é um projeto básico em Django que demonstra como renderizar duas páginas HTML:
  1. Página de inserção de URL de imagem: O usuário pode inserir uma URL de imagem e visualizá-la.
  2. Página de exibição de tabela a partir de CSV: Exibe uma tabela populada com dados de um arquivo CSV.

Pré-requisitos:
  Git
  Python 3.x
  pip

Como Executar o Projeto:
  1. Clone o Repositório:
    Execute no cmd <git clone https://github.com/LuanGFRicardo/Desafio-Django.git /caminho-de-preferencia>
  2. Instale as Dependências:
     pip install django
  3. Execute o Servidor de Desenvolvimento:
     Execute no cmd <cd /caminho-de-preferencia/Desafio-Django/desafio_django/>
     python manage.py runserver
  4. Acesse o Projeto no Navegador:
     http://127.0.0.1:8000/
  
Funcionalidades:
  Página Inicial: Contém dois botões para acessar as funcionalidades.
  Página de Inserção de Imagem: Insira a URL de uma imagem e clique em "Mostrar" para visualizá-la.
  Página de Exibição da Tabela: Mostra uma tabela populada com os dados do arquivo alunos.csv.

Estrutura do Desafio:
  |desafio_django/
        |principal/ # Diretório da aplicação Django
              |templates/ # Diretório de templates HTML
                    |principal/
                          |home.html # Página inicial
                          |image_url.html # Página de inserção de URL de imagem
                          |exibir_tabela.html # Página de exibição de tabela CSV
              |views.py # Arquivo com as views do desafio
              |urls.py # Arquivo de roteamento de URLs
                    |__init__.py # Arquivo de inicialização
  |manage.py # Script de gerenciamento do Django
  |alunos.csv # Arquivo CSV com os dados para a tabela
  |README.md # Intruções do projeto
