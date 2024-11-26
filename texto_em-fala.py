import pyttsx3

# Inicialize o mecanismo TTS
engine = pyttsx3.init()

# Defina o texto que você deseja que o Python fale
text = "Você está no Viva o Linux!"

# Fale o texto
engine.say(text)

# Aguarde até que a fala seja concluída antes de encerrar o programa
engine.runAndWait()