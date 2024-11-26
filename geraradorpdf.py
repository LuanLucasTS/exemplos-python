#pip install reportlab
from reportlab.pdfgen import canvas
import sqlite3

conexao = sqlite3.connect('arquivo.db', check_same_thread=False)

def GeneratePDF(lista):
    try:
        nome_pdf = 'teste'
        pdf = canvas.Canvas(f'{nome_pdf}.pdf')
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(10,x, f'{nome} : {idade}')
        pdf.setTitle(nome_pdf)
        pdf.setFont ("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Clientes')
        pdf.setFont ("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e Email')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')


list = conexao.execute("SELECT nome, email FROM usuarios").fetchall()
print(type(list))
print(list)

lista = dict.fromkeys(list)

#lista = {'Felipe': '24', 'Jose': '42', 'Maria': '22', 'Eduardo': '31'}


GeneratePDF(lista)

