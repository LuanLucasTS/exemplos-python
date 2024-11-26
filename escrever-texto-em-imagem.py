from PIL import Image, ImageDraw, ImageFont

# Abra a imagem existente
imagem = Image.open("assinatura.jpg")

# Crie um objeto ImageDraw para desenhar no topo da imagem
draw = ImageDraw.Draw(imagem)

# Especifique a fonte e o tamanho do texto
fonte_nome = ImageFont.truetype("LEMONMILK-Regular.otf", 30)
fonte_cargo = ImageFont.truetype("LEMONMILK-Regular.otf", 15)

# Especifique a posição e o texto que você deseja adicionar
posicao_nome = (439, 127)
texto_nome = "Luan Lucas"
posicao_cargo = (439, 161)
texto_cargo = "Cargo"



# Especifique a cor do texto (R, G, B)
cor_do_texto = (0, 0, 0)

# Adicione o texto à imagem
draw.text(posicao_nome, texto_nome, fill=cor_do_texto, font=fonte_nome)
draw.text(posicao_cargo, texto_cargo, fill=cor_do_texto, font=fonte_cargo)

# Salve a imagem com o texto
imagem.save("imagem_com_texto.jpg")

# Feche a imagem original
imagem.close()
