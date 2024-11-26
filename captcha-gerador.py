from captcha.image import ImageCaptcha

#configura a imagem
image = ImageCaptcha(width=280, height=90)

#Texto para o captcha
captcha_text = 'Python'

#Gera a imagem do captcha
data = image.generate(captcha_text)

#Salva a imagem
image.write(captcha_text, 'captcha.png')
