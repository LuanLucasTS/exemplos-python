import pyautogui
import time

def simular_digitar(mensagem):
    for letra in mensagem:
        pyautogui.typewrite(letra)
        time.sleep(0.1) # Pequena pausa entre as letras para simular a digitação

def enviar_mensagem():
    simular_digitar("Olá")
    pyautogui.press('enter') # Simula pressionar a tecla Enter para enviar

if __name__ == "__main__":
    print("Aguardando 10 segundos...")
    time.sleep(10)
    print("Enviando a primeira mensagem...")
    enviar_mensagem()

    while True:
        print("Aguardando 120 segundos para a próxima mensagem...")
        time.sleep(120)
        print("Enviando outra mensagem...")
        enviar_mensagem()