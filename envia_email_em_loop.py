import smtplib
from email.mime.text import MIMEText
import time

# Detalhes da sua conta de e-mail
seu_email = "suporte.ti.02@financial.com.br"  # Substitua pelo seu endereço de e-mail
sua_senha = "zawE*n@j44j6z&$cX5P"  # Substitua pela sua senha
destinatario_email = "tayane.pereira@telefonica.com"  # Substitua pelo e-mail do destinatário

def enviar_email(assunto, corpo, destinatario):
    try:
        # Cria a mensagem de e-mail
        mensagem = MIMEText(corpo)
        mensagem['Subject'] = assunto
        mensagem['From'] = seu_email
        mensagem['To'] = destinatario

        # Conecta ao servidor SMTP e inicia TLS
        with smtplib.SMTP('email-ssl.com.br', 587) as servidor:
            servidor.starttls()  # Inicia a criptografia TLS
            servidor.login(seu_email, sua_senha)
            servidor.sendmail(seu_email, destinatario, mensagem.as_string())
        print(f"E-mail enviado para {destinatario} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

if __name__ == "__main__":
    print("Aguardando 5 segundos...")
    time.sleep(5)
    print("Enviando o primeiro e-mail...")
    enviar_email("Vico tech", "Bom dia. Precisamos resolver a questão do vivo tech", destinatario_email)

    while True:
        print("Aguardando 120 segundos para o próximo e-mail...")
        time.sleep(120)
        print("Enviando outro e-mail...")
        enviar_email("Vico tech", "Bom dia. Precisamos resolver a questão do vivo tech", destinatario_email)