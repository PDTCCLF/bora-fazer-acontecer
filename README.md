# bora-fazer-acontecer

O **Bora Fazer Acontecer** é um sistema web administrativo para organização de eventos. Ele permite o cadastro, edição e organização de:

- **Eventos**
- **Participantes/Alunos**
- **Participações/Inscrições**
- **Voluntários**, que possuem o acesso ao sistema
- **Patrocinadores**
- **Financiamentos de eventos**

O sistema foi concebido principalmente para **voluntários de instituições sociais, culturais ou educacionais** que organizam e realizam atividades recreativas ou comunitárias. Também pode ser útil para estudantes e desenvolvedores iniciantes interessados em aprender sobre desenvolvimento de sistemas web organizacionais. Para mais detalhes, leia o <a href="https://github.com/PDTCCLF/bora-fazer-acontecer/wiki" target="_New"><b>wiki</b></a> do projeto. 

---

## Estrutura de Pastas e Arquivos
### Todos os arquivos listados são importantes para esse projeto, alguns não mencionados são gerados pelo próprio Django e ficaram inalterados, como explicado na observação abaixo.

- 📖 `README.md` — Documentação principal do projeto.  
- 📜 `requirements.txt` — Lista de dependências necessárias para rodar o projeto.  
- 📄 `manage.py` — Script de gerenciamento do Django (migrations, runserver, etc.), necessário para execução do software.  
- 📂 `bora_fazer_acontecer/` — Diretório principal do projeto Django, contendo configurações, utilitários e arquivos centrais da aplicação.  
  - ⚙️ `.env` — Os campos devem ser preenchidos com credenciais de acesso ao banco de dados e a senha de acesso ao ambiente de produção usada em `base.py`.
  - 📄 `asgi.py` — Ponto de entrada para a execução assíncrona do projeto, usado em servidores compatíveis com ASGI. Gerado pelo Django e sem alterações.
  - 📄 `urls.py` — Arquivo que centraliza as rotas do sistema, conectando URLs às views correspondentes.
  - 📄 `utils.py` — Arquivo com função utilitária para geração de IDs únicos pros dados.
  - 📄 `wsgi.py` — Ponto de entrada para a execução síncrona do projeto, usado em servidores compatíveis com WSGI. Gerado pelo Django e sem alterações.
  - 📂 `settings/` — Diretório de configurações, separado por ambientes.
    - 📄 `__init__.py` — Como `settings.py` padrão foi trocado por uma pasta para separar as configurações entre ambiente de produção e dev, é necessário incluir esse arquivo.
    - 📄 `base.py` — Configurações comuns e compartilhadas entre todos os ambientes do projeto.
    - 📄 `dev.py` — Configurações específicas para o ambiente de desenvolvimento (modo debug ativo, que abre um link na home page para o painel admin Django).
    - 📄 `prod.py` — Configurações específicas para o ambiente de produção.
  - 📂 `static/` — Diretório com arquivos estáticos acessíveis pela aplicação (CSS e imagens).
    - 📂 `css/` — Diretório para folhas de estilo CSS.
      - 🎨 `style.css` — Folha de estilos principal usada para padronizar a aparência do sistema.
- 📂 `base/` — App que contém a classe abstrata **Base**, herdada por outros models.
  - 📄 `models.py` — Modelo da entidade **Base**. 
- 📂 `core/` — App responsável pela página inicial e configurações gerais.
  - 📄 `urls.py` — Define as rotas específicas de login, logout e a home page, conectando-as às views.
  - 📄 `views.py` — Implementa a lógica das páginas iniciais do sistema, incluindo autenticação e exibição da home.
  - 📂 `fixtures/` — Pasta para arquivos de dados de exemplo e/ou teste para inserção no banco.
    - 📑 `sample_data.json` — Arquivo com dados genéricos de todas as entidades do sistema.
  - 📂 `management/` — Pasta especial do Django para comportar comandos customizados de linha de comando. Inclua um `__init__.py` na pasta.
    - 📂 `commands/` — Diretório onde ficam os arquivos de comandos definidos pelo desenvolvedor. Inclua um `__init__.py` na pasta.
      - 📄 `reset_data.py` — Comando customizado que permite apagar os dados do banco sem excluir usuários administrativos (superusuários).  
  - 📂 `static/`
    - 📂 `core/` 
      - 📂 `css/`
        - 🎨 `style.css` 
  - 📂 `templates/`
    - 📂 `core/`
      - 🌐 `home.html` — Template da página inicial exibida após o login.
      - 🌐 `login.html` — Template da página de autenticação de usuários voluntários.
  - 📂 `tests/`
    - 📄 `test_views.py` — Contém testes automatizados para validar o comportamento das views do app **Core**.
- 📂 `pessoas/` — App para gerenciar **Alunos** e **Voluntários**.
  - 📄 `admin.py` — Configurações para registro e administração das entidades no Django Admin.
  - 📄 `forms.py` — Formulários de cadastro/edição e validação de dados.  
  - 📄 `models.py` — Modelos das entidades.  
  - 📄 `urls.py` — Define as rotas específicas do app **Pessoas**.
  - 📄 `views.py` — Lógica de CRUD de **Alunos** e **Voluntários**.
  - 📂 `static/`
    - 📂 `pessoas/` — Diretório-namespace dos arquivos estáticos do app **Pessoas**, evitando conflito de nomes com outros apps.
      - 📂 `css/`
        - 🎨 `style.css` — Folha de estilos usada pelas páginas de **Alunos** e **Voluntários**.
  - 📂 `templates/` — Páginas HTML utilizadas pelo sistema.
    - 📂 `pessoas/` — Diretório-namespace dos templates do app **Pessoas**, evitando conflito de nomes com outros apps.
      - 📂 `alunos/` — Subpasta com os templates de **Alunos**.
        - 🌐 `lista.html` — Página de listagem de **Alunos** cadastrados.
        - 🌐 `formulario.html` — Página de formulário para criação e edição de **Alunos**.
        - 🌐 `confirma_deletar.html` — Página de confirmação para exclusão de um aluno.
      - 📂 `voluntarios/`
        - 🌐 `lista.html`
        - 🌐 `formulario.html`
        - 🌐 `confirma_deletar.html`
  - 📂 `tests/` — Testes unitários e de integração do app.
    - 📄 `test_forms.py` — Contém testes automatizados para validar o comportamento dos forms do app **Pessoas**.
    - 📄 `test_models.py` — Contém testes automatizados para validar o comportamento dos models do app **Pessoas**.  
    - 📄 `test_views.py` — Contém testes automatizados para validar o comportamento das views do app **Pessoas**.  
- 📂 `eventos/` — App para gerenciar **Eventos** e **Participações**.  
  - 📄 `admin.py`
  - 📄 `forms.py`
  - 📄 `models.py`
  - 📄 `urls.py`
  - 📄 `views.py`
  - 📂 `static/`
    - 📂 `eventos/` 
      - 📂 `css/`
        - 🎨 `style.css`
  - 📂 `templates/`
    - 📂 `eventos/`
      - 🌐 `lista.html` 
      - 🌐 `formulario.html`
      - 🌐 `confirma_deletar.html`
      - 🌐 `participacoes.html` — HTML de página da lista de **Participações**.
      - 🌐 `formulario_participacao.html`
      - 🌐 `confirma_deletar_participacao.html`
  - 📂 `tests/`
    - 📄 `test_forms.py`
    - 📄 `test_models.py`  
    - 📄 `test_views.py`
- 📂 `patrocinadores/` — App para gerenciar **Patrocinadores** e **Financiamentos de Eventos**.  
  - 📄 `admin.py`
  - 📄 `forms.py`
  - 📄 `models.py`
  - 📄 `urls.py`
  - 📄 `views.py`
  - 📂 `static/`
    - 📂 `patrocinadores/` 
      - 📂 `css/`
        - 🎨 `style.css`
  - 📂 `templates/`
    - 📂 `patrocinadores/`
      - 🌐 `lista.html` 
      - 🌐 `formulario.html`
      - 🌐 `confirma_deletar.html`
      - 🌐 `financiamentos.html` — HTML de página da lista de **Financiamentos de Eventos**.
      - 🌐 `formulario_financiamento.html`
      - 🌐 `confirma_deletar_financiamento.html`
  - 📂 `tests/`
    - 📄 `test_forms.py`
    - 📄 `test_models.py`  
    - 📄 `test_views.py`

Observação: Cada app (nesse projeto, são **Base**, **Core**, **Eventos**, **Pessoas** e **Patrocinadores**) possui os seguintes arquivos gerados pelo Django: pasta `migrations`, `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py` e `__init__.py`. Como `tests.py` padrão foi trocado por uma pasta `tests/` (em todos os apps exceto o **Base**) para modularizar os testes em mais de um arquivo, é necessário incluir o arquivo `__init__.py` na pasta `tests/` de cada. Ele marca um diretório como um pacote Python comum e permite que seus módulos sejam importados por outros arquivos.

**Legenda:**
- 📂 Diretório  
- 📄 Arquivo Python (.py)
- 🌐 Arquivo HTML (.html)
- 🎨 Arquivo CSS (.css)
- 📖 Arquivo Markdown (.md)  
- 📜 Arquivo de texto (.txt)
- 📑 Arquivo JSON (.json)
- ⚙️ Arquivo de variáveis de ambiente (.env)

---

## Pré-requisitos 

### Tecnologias utilizadas
Para utilizar este projeto, é necessário instalar as seguintes dependências:  
- **Python** (versão >= 3.12)
- **Pip** (versão >= 25.1)  
- **Django** (versão >= 5.2)  
- **PostgreSQL** (versão >= 17.3)

### Como instalar
As instruções a seguir são para o sistema operacional **Windows**, onde foi testado. Caso utilize outro SO, por favor procure o equivalente dessas instruções.

#### **1. Instalar Python**  
1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Baixe o instalador da versão mais recente.  
3. Durante a instalação, **marque a opção "Add Python to PATH"** para facilitar o uso do Python no terminal.  
4. Finalize a instalação e reinicie o computador, se necessário.  
5. Abra o **Prompt de Comando (cmd)**.  
6. Verifique se o Python foi instalado corretamente:  
   ```sh
   python --version
   ```  
   Se o comando exibir a versão do Python, a instalação foi bem-sucedida. Caso contrário, revise os passos anteriores.  
7. Caso não esteja instalado ou queira atualizá-lo, repita os passos acima baixando a versão mais recente do site oficial. 

#### **2. Instalar Pip**  
Após instalar o Python, o Pip deve vir incluído. Para garantir que está disponível:  
1. Abra o **Prompt de Comando (cmd)**.  
2. Verifique se o Pip está instalado corretamente:  
   ```sh
   pip --version
   ```  
   Se o comando exibir a versão do Pip, a instalação foi bem-sucedida. Caso contrário, prossiga com a atualização:  
3. Caso não esteja instalado ou queira atualizá-lo, execute o seguinte comando:  
   ```sh
   python -m pip install --upgrade pip
   ```  

#### **3. Instalar Django** 
1. Certifique-se de que está no seu ambiente virtual (recomendado) ou diretamente no sistema.
2. No terminal, instale o Django com: 
   ```sh
   pip install django
   ```
3. Verifique se a instalação foi bem-sucedida:
   ```sh
   python -m django --version
   ```
Se aparecer a versão instalada, o Django está pronto para uso.

#### **4. Instalar PostgreSQL**
1. Acesse o site oficial: https://www.postgresql.org/download/
2. Baixe o instalador compatível com seu sistema operacional.
3. Durante a instalação, configure:
- Um usuário padrão (normalmente postgres).
- Uma senha para este usuário (anote para usar no .env).
- A porta de conexão (por padrão, 5432).
4. Finalize a instalação e reinicie o computador, se necessário. Abra o pgAdmin ou use o terminal psql para verificar.
5. Confirme a versão instalada com:
   ```sh
   psql --version
   ```
6. Caso o comando não funcione, verifique se o PostgreSQL foi adicionado como variável de ambiente ao PATH do sistema. Caso contrário, adicione o caminho do diretório `bin` do PostgreSQL (exemplo: `C:\Program Files\PostgreSQL\17\bin`) às variáveis de ambiente do sistema e reinicie o computador.

#### **5. Criar Banco de Dados e Usuário**
1. No terminal, conecte-se como usuário administrador:
   ```sh
   psql -U postgres
   ```
2. Dentro do console PostgreSQL (basta executar o comando anterior), crie o banco de dados (substitua nome_do_banco por um nome de sua escolha):
   ```sh
   CREATE DATABASE nome_do_banco;
   ```
3. Crie um usuário do PostgreSQL (substitua username e senha por nomes de sua escolha):
   ```sh
   CREATE USER username WITH PASSWORD 'senha';
   ```
4. Dê privilégios ao usuário no banco de dados (substitua nome_db e username pelos nomes que usou nos passos anteriores):
   ```sh
   GRANT ALL PRIVILEGES ON DATABASE nome_db TO username;
   ```
5. Permita que o usuário possa criar bancos (necessário em alguns cenários de testes/migrações, substitua username pelo nome que usou nos passos anteriores):
   ```sh
   ALTER USER username CREATEDB;
   ```
6. Conecte-se ao banco criado (substitua nome_db pelo nome que usou nos passos anteriores):
   ```sh
   \c nome_db
   ```
7. Garanta que o usuário tenha acesso ao schema público (substitua username pelo nome que usou nos passos anteriores):
   ```sh
   GRANT ALL ON SCHEMA public TO username;
   ```
8. Saia do console PostgreSQL:
   ```sh
   \q
   ```
    Observação: Após acessar o site e criar dados, caso queira voltar ao console PostgreSQL e rodar consultas diretas no banco de dados, digite no terminal (substitua nome_db e username pelos nomes que usou nos passos anteriores):
   ```sh
   psql -U username -d nome_db
   ```

---

## Como Executar
1. Clone o repositório:  
   ```bash
   git clone https://github.com/PDTCCLF/bora-fazer-acontecer.git
   ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
    Observação: O segundo venv no comando pode ser trocado por um nome de sua preferência pro ambiente virtual.
3. Ative o ambiente virtual criado (caso tenha dado outro nome pro ambiente virtual, use-o no lugar do venv no comando abaixo):
    ```bash
    venv\Scripts\activate
    ```
    Observação: Se tiver funcionado, o nome do ambiente virtual (venv nesse caso) aparecerá no início da linha de comando. Se não for, tente rodar 
    ```bash
    Set-ExecutionPolicy RemoteSigned
    ```
    e refaça esse passo.
4. Instale as dependências de bibliotecas Python:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure o arquivo `.env` com as informações necessárias (no próprio arquivo, encontram-se orientações para preenchimento). 
6. Execute as migrações:
    ```bash
    python manage.py migrate
    ```
7. Crie um superusuário para acessar o sistema:
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para definir o nome de usuário, e-mail (opcional) e senha.
8. Execute o servidor:

    Para rodar no ambiente de desenvolvimento,
    ```bash
    python manage.py runserver --settings=bora_fazer_acontecer.settings.dev
    ```
    Para rodar no ambiente de produção,
    ```bash
    python manage.py runserver --settings=bora_fazer_acontecer.settings.prod
    ```
9. Acesse o sistema via browser:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Se o front-end não tiver carregado, mostrando o site sem o layout, tente recarregar a página usando Ctrl + Shift + R. Se isso não funcionar, tente rodar o site no outro ambiente (dev ou prod) ou trocar de navegador.
10. Faça login no site com o superusuário criado no passo 7.
11. Explore o sistema! No <a href="https://github.com/PDTCCLF/bora-fazer-acontecer/wiki#manual-de-utiliza%C3%A7%C3%A3o-para-usu%C3%A1rios-contemplados" target="_New"><b>wiki</b></a> do projeto, há um guia de uso detalhado.

    Extra: Caso queira testar o site sem ter que cadastrar dados manualmente, pode carregar os dados de exemplo disponíveis no arquivo `sample_data.json` com o comando:
    ```bash
    python manage.py loaddata sample_data.json
    ```
    Isso criará dados genéricos para todas as entidades do sistema. Também é fácil remover os dados e recomeçar com o comando:
    ```bash
    python manage.py reset_data
    ```

---

### Testes
Para executar os testes unitários e de integração, digite no terminal:
```bash
python manage.py test
```

---

## Licença

Projeto acadêmico para fins educacionais e demonstrativos. Não deve ser usado em produção sem adaptações.  
Este projeto é disponibilizado sob a licença <a href="https://opensource.org/license/MIT" target="_New"><b>**MIT**</b></a>, que permite que qualquer pessoa utilize, copie, modifique e distribua o código.