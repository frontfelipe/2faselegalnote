# 2faseleganote
Teste para a segunda etapa do processo seletivo LegalNote

#Objetivo
Entregar uma API usando DJANGO-REST-FRAMEWORK que usa o model de Users do Django e vocês terão que criar um model de Processos (contendo numero_processo - 20 caractereres numéricos, dados do processo um campo text field )

Cada Usuário pode ter vários processos.

Cada vez que um processo for cadastrado o sistema precisa enviar um email (Pode usar o console Backend e mostrar o email no terminal se quiser)

#Requirements
Django==1.8.4

djangorestframework==3.2.3

#Setup BD
Neste teste utilizei SQLITE3

#Initial Data
Caso queira já testar a aplicacao, foi criado uma fixture com dados iniciais

Comando: python manage.py loaddata /teste/fixtures/initial_data.json

#Email localhost
Execute o comando a seguir para iniciar o servidor localhost de email

python -m smtpd -n -c DebuggingServer localhost:587

