import imaplib
import email
from email.header import decode_header

# Configuração de conexão
username = "seu_email@gmail.com"      # Insira seu e-mail
password = "sua_senha"                # Insira sua senha
imap_server = "imap.gmail.com"        # Use o servidor IMAP do seu provedor

# Conectando ao servidor IMAP
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)

# Seleciona a caixa de entrada
mail.select("inbox")

# Busca por e-mails não lidos
status, messages = mail.search(None, 'UNSEEN')
email_ids = messages[0].split()

# Lendo os e-mails
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            print("Assunto:", subject)

            # Obter remetente
            from_ = msg.get("From")
            print("De:", from_)

            # Extrair o corpo do e-mail
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        print("Corpo:", body)
            else:
                body = msg.get_payload(decode=True).decode()
                print("Corpo:", body)

# Fecha a conexão
mail.logout()
