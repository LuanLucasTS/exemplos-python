import pytesseract
from PIL import Image

# Define o caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Carrega a imagem
imagem = Image.open('D:\\Luan\\Downloads\\python.jpg')

# Extrai o texto da imagem
texto_extraido = pytesseract.image_to_string(imagem)

# Imprime o texto extraído
print(texto_extraido)