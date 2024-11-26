import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Configurações de gravação
duration = 10  # segundos
filename = "output.wav"

# Função para capturar o áudio
def record_audio(filename, duration):
    print("Gravando...")
    # Captura o áudio do dispositivo de saída padrão
    recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
    sd.wait()  # Espera até que a gravação esteja completa
    print("Gravação concluída.")
    # Salva o áudio em um arquivo WAV
    wav.write(filename, 44100, recording)

# Chama a função para gravar o áudio
record_audio(filename, duration)
