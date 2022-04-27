"""
cd = (mudar pastas)
dir = (listar pastas)
mkdir = (criar pastas/arquivos)
del = (deletar arquivos)
rmdir = (deletar a pasta com todos seus arquivos)
cls = (limpar a tela)
Tecla Tab = (alto completa um nome na hora de digitar)


Comandos
git init (iniciar repositorio no git)
git add (mover arquivos e dar inicio ao versionamento)
git commit (criar commites)


Criando um repositório
git init = Efetuar esse comando para criar uma pasta oculta .git
ls -a = (mostrar arquivos e pastas ocultas)


Adicionando um Arquivo
git add * = Comando para adicionar as alterações feitas em todos os arquivos do projeto
git commit -m "" = Comando para fazer um commit do seu projeto (colocar uma mensagem dentro das strings "")


Servidor
Remote Repository (Quando você empurra um commit para um repositório)


Ambiente de desenvolvimento
Working Directory (Seu Computador)
Staging Area (Quando criado, modificado ou adicionado um arquivo no Git)
Local Repository (Quando é efetuado um Commit)


Comando para configurar seu perfil no GIT
git config --global --unset user.email (comando para limpar o seu email no perfil)
git config --global --unset user.nickname (comando para limpar o seu user no perfil)
git config --list (comando para ver a lista de configurações)
git config --global user.email "seu email"(comando para adicionar o seu email no perfil)
git config --global user.nickname "seu nome"(comando para adicionar o seu user no perfil)



Configuração do seu Repositório no GIT
git remote add origin (link do seu repositório GitHub) = comando para adicionar seu repositório GitHub a sua maquina local
origin = apelido do seu link repositório
git remote -v = Comando para listar seus repositórios cadastrados
git push origin master = Comando para empurrar seu repositório local para o remoto


Comando para configurar seu perfil no GIT
git config --global --unset user.email (comando para limpar o seu email no perfil)
git config --global --unset user.nickname (comando para limpar o seu user no perfil)
git config --list (comando para ver a lista de configurações)
git config --global user.email "seu email"(comando para adicionar o seu email no perfil)
git config --global user.nickname "seu nome"(comando para adicionar o seu user no perfil)


Configuração do seu Repositório no GIT
git remote add origin (link do seu repositório GitHub) = comando para adicionar seu repositório GitHub a sua maquina local
origin = apelido do seu link repositório
git remote -v = Comando para listar seus repositórios cadastrados
git push origin master = Comando para empurrar seu repositório local para o remoto


Resolvendo conflitos
Como os conflitos acontecem no GitHub e como resolvê-los
git pull origin master = Comando para puxar um conteúdo do seu repositório remoto
"""