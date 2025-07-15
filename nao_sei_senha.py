from pypdf import PdfReader
from tqdm import tqdm  # para barra de progresso

pdf_path = "C:/Users/luan.silva/Downloads/boleto/S2110404250714A.pdf"
reader = PdfReader(pdf_path)

# Gera todas as combinações de 000000 a 999999
for i in tqdm(range(1000000), desc="Tentando senhas"):
    senha = f"{i:06d}"  # Formata como 6 dígitos (ex: 000123)
    try:
        if reader.decrypt(senha):
            print(f"\n✅ Senha encontrada: {senha}")
            break
    except Exception:
        continue
else:
    print("\n❌ Senha não encontrada.")
