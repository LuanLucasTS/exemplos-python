import easyocr

#Define o idioma
reader = easyocr.Reader(['pt'])

#Carrega e faz a leitura da imagem
results = reader.readtext('D:/Luan/Downloads/2.jpg', paragraph=True)

#Mostra o resultado
for result in results:
    print(f'{result[1]}')
