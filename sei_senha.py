from pypdf import PdfReader, PdfWriter

# Caminho do PDF original e do PDF sem senha
pdf_com_senha = "C:/Users/luan.silva/Downloads/boleto/S2110404250714A.pdf"
pdf_sem_senha = "C:/Users/luan.silva/Downloads/boleto/arquivo_sem_senha.pdf"

# Abre o PDF com senha
reader = PdfReader(pdf_com_senha)
reader.decrypt("121858")

# Cria um novo PDF writer
writer = PdfWriter()

# Adiciona todas as páginas do PDF original ao novo writer
for page in reader.pages:
    writer.add_page(page)

# Escreve o novo arquivo sem proteção
with open(pdf_sem_senha, "wb") as f:
    writer.write(f)

print("PDF salvo sem senha com sucesso!")
