from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models import signals
from django.db.models.signals import post_save



class Processos(models.Model):
    user = models.ForeignKey(User)
    num_processo = models.IntegerField(u'Numero do Processo')
    dados_processo = models.TextField(u'Dados do Processo')
    data_pub = models.DateTimeField(auto_now_add=True) 

    def __unicode__(self):
        return self.data_pub
    
    class Meta:
        verbose_name = u'Processos'


##### SIGNAL P/ ENVIO DE EMAIL #####
def send_email(sender, **kwargs):
	email = EmailMessage('Processo Cadastrado', 'Um processo foi cadastrado em sua conta !!!', to=['teste@teste.com'])
	email.send()
	
post_save.connect(send_email, sender=Processos)