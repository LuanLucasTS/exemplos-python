import pyautogui
import time
from faker import Faker


pyautogui.alert("O código vai começar. Não faça nada até terminar!")
time.sleep(10)
pyautogui.PAUSE = 0.1

fake = Faker()

for i in range(1000):
    ipv6=fake.ipv6()
    pyautogui.write(ipv6)
    pyautogui.press('enter')

pyautogui.alert(" Finalizado")


