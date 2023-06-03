# Projeto Django: Project1<br>
Este é o repositório do projeto Django Project1. O projeto utiliza técnicas como o slugify para tratar dados antes de salvá-los no banco de dados. Ele permite o cadastro de produtos, incluindo imagens, e exibe essas imagens na interface do usuário. Além disso, possui uma aba de contato que permite o envio de emails para se comunicar com os usuários.<br><br>

Configuração<br>
Para executar o projeto localmente, siga as etapas abaixo:<br>

Clone o repositório em sua máquina local:<br>

shell<br>
Copy code<br>
git clone https://github.com/lazarowend/project1-django.git<br>
cd project1-django<br>
Crie um ambiente virtual para isolar as dependências do projeto:<br><br>

shell<br>
Copy code<br>
python -m venv myenv<br>
Ative o ambiente virtual:<br>

shell<br>
Copy code<br>
# No Windows<br>
myenv\Scripts\activate<br><br>

# No macOS/Linux<br>
source myenv/bin/activate<br>
Instale as dependências necessárias:<br>

shell<br>
Copy code<br>
pip install -r requirements.txt<br>
Realize as migrações do banco de dados:<br><br>

shell<br>
Copy code<br>
python manage.py migrate<br>
Execute o servidor de desenvolvimento:<br><br>

shell<br>
Copy code<br>
python manage.py runserver<br>
Acesse o projeto em seu navegador em http://localhost:8000.<br><br>

Funcionalidades<br>
Cadastro de Produtos<br>
O projeto permite o cadastro de produtos através de um formulário. Cada produto possui informações como nome, descrição e imagem. O nome do produto é tratado com a técnica de slugify antes de ser salvo no banco de dados, garantindo que seja um formato amigável para URL.<br><br>

Exibição de Imagem do Produto<br>
Ao visualizar um produto na interface do usuário, a imagem associada a ele é exibida. Isso permite que os usuários vejam uma representação visual do produto.<br><br>

Aba de Contato<br>
O projeto possui uma aba de contato que permite que os usuários enviem mensagens através de um formulário. Quando uma mensagem é enviada, um email é disparado para a equipe responsável. Isso facilita a comunicação entre os usuários e o administrador do sistema.<br><br>

Estrutura do Projeto<br>
A estrutura do projeto é organizada da seguinte forma:<br>
project1-django/<br>
├── core/<br>
│   ├── migrations/<br>
│   ├── static/<br>
│   ├── templates/<br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── project1/<br>
│   ├── __init__.py<br>
│   ├── asgi.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   └── wsgi.py<br>
├── media/produtos/<br>
├── .gitignore<br>
├── manage.py<br>
└── requirements.txt<br><br>
A pasta core/ contém os arquivos relacionados ao aplicativo Django, como modelos (models.py), visualizações (views.py) e URLs (urls.py).<br>
A pasta media/ é usada para armazenar as imagens dos produtos.<br>
A pasta static/ contém os arquivos estáticos do projeto, como folhas de estilo CSS e arquivos JavaScript.<br>
O arquivo .gitignore lista os arquivos e pastas que devem ser ignor
