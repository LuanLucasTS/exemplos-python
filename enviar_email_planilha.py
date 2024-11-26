import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

planilha = pd.read_excel('usuarios.xls')

email_usuario = 'ENDEREÇO_EMAIL'
senha_usuario = 'SENHA_EMAIL'
servidor_smtp = 'SERVIDOR_EMAIL'
porta_smtp = 587

assunto = 'Informações de Acesso ao novo sistema de chamado'
mensagem_template = 'CORPO_DA_MENSAGEM'

server = smtplib.SMTP(servidor_smtp, porta_smtp)
server.starttls()
server.login(email_usuario, senha_usuario)

for indice, linha in planilha.iterrows():
    email_destino = linha['email']
    usuario_planilha = linha['usuário']
    senha_planilha = linha['senha']

    mensagem = MIMEMultipart()
    mensagem['From'] = email_usuario
    mensagem['To'] = email_destino
    mensagem['Subject'] = assunto

    corpo_mensagem = mensagem_template.format(usuario=usuario_planilha, senha=senha_planilha)
    mensagem.attach(MIMEText(corpo_mensagem, 'plain'))

    server.sendmail(email_usuario, email_destino, mensagem.as_string())

server.quit()