# 1. Escreva uma função soma(a, b) que receba dois números e retorne a soma deles.
def soma(a, b):
    return a + b

# Teste da função soma
print(soma(5, 3))  # Saída: 8


# 2. Crie uma função maior(a, b) que receba dois números e retorne o maior entre eles.
def maior(a, b):
    if a > b:
        return a
    else:
        return b

# Teste da função maior
print(maior(5, 3))  # Saída: 5


# 3. Escreva uma função eh_par(numero) que receba um número e retorne True se ele for par e False caso contrário.
def eh_par(numero):
    return numero % 2 == 0

# Teste da função eh_par
print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False


# 4. Implemente uma função quadrado(x) que receba um número e retorne o seu quadrado.
def quadrado(x):
    return x ** 2

# Teste da função quadrado
print(quadrado(4))  # Saída: 16


# 5. Crie uma função mult_tres_numeros(a, b, c) que multiplica três números e retorna o resultado.
def mult_tres_numeros(a, b, c):
    return a * b * c

# Teste da função mult_tres_numeros
print(mult_tres_numeros(2, 3, 4))  # Saída: 24


# 6. Escreva uma função fatorial(n) que calcule o fatorial de um número inteiro n.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Teste da função fatorial
print(fatorial(5))  # Saída: 120


# 7. Crie uma função conta_vogais(texto) que retorne o número de vogais em uma string.
def conta_vogais(texto):
    return sum(1 for letra in texto if letra.lower() in "aeiou")

# Teste da função conta_vogais
print(conta_vogais("Olá Mundo"))  # Saída: 4


# 8. Implemente uma função inverte_string(s) que retorne a string s invertida.
def inverte_string(s):
    return s[::-1]

# Teste da função inverte_string
print(inverte_string("Python"))  # Saída: "nohtyP"


# 9. Escreva uma função fatorial(n) que calcule o fatorial de um número inteiro n.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Teste da função fatorial
print(fatorial(5))  # Saída: 120


# 10. Crie uma função eh_primo(n) que verifique se um número é primo.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Teste da função eh_primo
print(eh_primo(7))  # Saída: True
print(eh_primo(10))  # Saída: False

# 11. Crie uma função conta_palavras(texto) que conte quantas palavras existem em uma string.
def conta_palavras(texto):
    return len(texto.split())

# Teste da função conta_palavras
print(conta_palavras("Eu gosto de Python"))  # Saída: 4


# 12. Escreva uma função eh_palindromo(s) que verifique se uma palavra ou frase é um palíndromo.
def eh_palindromo(s):
    s = s.replace(" ", "").lower()  # Remove espaços e coloca em minúsculas
    return s == s[::-1]

# Teste da função eh_palindromo
print(eh_palindromo("arara"))  # Saída: True
print(eh_palindromo("python"))  # Saída: False


# 13. Implemente uma função conta_letras(s, letra) que conte quantas vezes uma determinada letra aparece em uma string.
def conta_letras(s, letra):
    return s.count(letra)

# Teste da função conta_letras
print(conta_letras("banana", "a"))  # Saída: 3


# 14. Crie uma função capitaliza_palavras(texto) que capitaliza a primeira letra de cada palavra em um texto.
def capitaliza_palavras(texto):
    return " ".join([palavra.capitalize() for palavra in texto.split()])

# Teste da função capitaliza_palavras
print(capitaliza_palavras("olá mundo"))  # Saída: "Olá Mundo"


# 15. Escreva uma função ocorrencias_palavras(texto) que retorne um dicionário com a contagem de cada palavra em um texto.
def ocorrencias_palavras(texto):
    palavras = texto.split()
    return {palavra: palavras.count(palavra) for palavra in palavras}

# Teste da função ocorrencias_palavras
print(ocorrencias_palavras("python é legal e python é divertido"))
# Saída: {'python': 2, 'é': 2, 'legal': 1, 'e': 1, 'divertido': 1}


# 16. Crie uma função retira_espacos(texto) que retorne uma string sem espaços em branco.
def retira_espacos(texto):
    return texto.replace(" ", "")

# Teste da função retira_espacos
print(retira_espacos("python é legal"))  # Saída: "pythonélegal"


# 17. Implemente uma função encontra_palavra(texto, palavra) que retorne o índice da primeira ocorrência de uma palavra em uma string.
def encontra_palavra(texto, palavra):
    return texto.find(palavra)

# Teste da função encontra_palavra
print(encontra_palavra("Eu gosto de Python", "Python"))  # Saída: 12


# 18. Escreva uma função alterna_maiusculas(texto) que alterne as letras para maiúsculas e minúsculas.
def alterna_maiusculas(texto):
    return "".join([letra.upper() if i % 2 == 0 else letra.lower() for i, letra in enumerate(texto)])

# Teste da função alterna_maiusculas
print(alterna_maiusculas("python"))  # Saída: "PyThOn"


# 19. Crie uma função apaga_vogais(s) que remova todas as vogais de uma string.
def apaga_vogais(s):
    return "".join([letra for letra in s if letra not in "aeiouAEIOU"])

# Teste da função apaga_vogais
print(apaga_vogais("banana"))  # Saída: "bn"


# 20. Implemente uma função troca_vogais(s, nova_letra) que substitua todas as vogais de uma string por uma nova letra.
def troca_vogais(s, nova_letra):
    return "".join([nova_letra if letra in "aeiouAEIOU" else letra for letra in s])

# Teste da função troca_vogais
print(troca_vogais("banana", "x"))  # Saída: "bxnxnx"

# 21. Crie uma função media_lista(lista) que receba uma lista de números e retorne a média.
def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0

# Teste da função media_lista
print(media_lista([1, 2, 3, 4, 5]))  # Saída: 3.0
print(media_lista([]))  # Saída: 0


# 22. Escreva uma função maior_elemento(lista) que retorne o maior número de uma lista.
def maior_elemento(lista):
    return max(lista) if lista else None

# Teste da função maior_elemento
print(maior_elemento([1, 2, 3, 4, 5]))  # Saída: 5
print(maior_elemento([]))  # Saída: None


# 23. Implemente uma função menor_elemento(lista) que retorne o menor número de uma lista.
def menor_elemento(lista):
    return min(lista) if lista else None

# Teste da função menor_elemento
print(menor_elemento([1, 2, 3, 4, 5]))  # Saída: 1
print(menor_elemento([]))  # Saída: None


# 24. Crie uma função conta_ocorrencias(lista, elemento) que conta quantas vezes um elemento aparece em uma lista.
def conta_ocorrencias(lista, elemento):
    return lista.count(elemento)

# Teste da função conta_ocorrencias
print(conta_ocorrencias([1, 2, 3, 2, 2, 4], 2))  # Saída: 3
print(conta_ocorrencias([1, 2, 3, 4], 5))  # Saída: 0


# 25. Escreva uma função remove_duplicados(lista) que retorne uma lista sem elementos duplicados.
def remove_duplicados(lista):
    return list(set(lista))

# Teste da função remove_duplicados
print(remove_duplicados([1, 2, 2, 3, 3, 4]))  # Saída: [1, 2, 3, 4]


# 26. Crie uma função soma_pares(lista) que retorne a soma de todos os números pares em uma lista.
def soma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)

# Teste da função soma_pares
print(soma_pares([1, 2, 3, 4, 5, 6]))  # Saída: 12


# 27. Implemente uma função elementos_unicos(lista) que retorne uma lista com os elementos únicos.
def elementos_unicos(lista):
    return [x for x in lista if lista.count(x) == 1]

# Teste da função elementos_unicos
print(elementos_unicos([1, 2, 2, 3, 4, 4]))  # Saída: [1, 3]


# 28. Escreva uma função lista_invertida(lista) que retorne a lista invertida.
def lista_invertida(lista):
    return lista[::-1]

# Teste da função lista_invertida
print(lista_invertida([1, 2, 3, 4, 5]))  # Saída: [5, 4, 3, 2, 1]


# 29. Crie uma função intersecao_listas(lista1, lista2) que retorne os elementos em comum entre duas listas.
def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Teste da função intersecao_listas
print(intersecao_listas([1, 2, 3], [3, 4, 5]))  # Saída: [3]


# 30. Implemente uma função uniao_listas(lista1, lista2) que retorne a união de duas listas.
def uniao_listas(lista1, lista2):
    return list(set(lista1) | set(lista2))

# Teste da função uniao_listas
print(uniao_listas([1, 2, 3], [3, 4, 5]))  # Saída: [1, 2, 3, 4, 5]

# 31. Escreva uma função potencia(base, expoente) que calcule base elevado a expoente.
def potencia(base, expoente):
    return base ** expoente

# Teste da função potencia
print(potencia(2, 3))  # Saída: 8
print(potencia(5, 0))  # Saída: 1


# 32. Crie uma função raiz_quadrada(n) que retorne a raiz quadrada de um número.
import math
def raiz_quadrada(n):
    return math.sqrt(n)

# Teste da função raiz_quadrada
print(raiz_quadrada(16))  # Saída: 4.0
print(raiz_quadrada(25))  # Saída: 5.0


# 33. Implemente uma função area_circulo(raio) que calcule a área de um círculo de raio r.
def area_circulo(raio):
    return math.pi * raio ** 2

# Teste da função area_circulo
print(area_circulo(3))  # Saída: 28.274333882308138


# 34. Escreva uma função hipotenusa(a, b) que calcule a hipotenusa de um triângulo retângulo.
def hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# Teste da função hipotenusa
print(hipotenusa(3, 4))  # Saída: 5.0
print(hipotenusa(5, 12))  # Saída: 13.0


# 35. Crie uma função area_triangulo(base, altura) que calcule a área de um triângulo.
def area_triangulo(base, altura):
    return (base * altura) / 2

# Teste da função area_triangulo
print(area_triangulo(4, 6))  # Saída: 12.0
print(area_triangulo(5, 10))  # Saída: 25.0


# 36. Implemente uma função eh_perfeito(n) que verifica se um número é um número perfeito.
def eh_perfeito(n):
    divisores = [i for i in range(1, n) if n % i == 0]
    return sum(divisores) == n

# Teste da função eh_perfeito
print(eh_perfeito(6))  # Saída: True (6 é perfeito)
print(eh_perfeito(10))  # Saída: False


# 37. Escreva uma função eh_armstrong(n) que verifica se um número é um número de Armstrong.
def eh_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    soma = sum(int(digit) ** num_len for digit in num_str)
    return soma == n

# Teste da função eh_armstrong
print(eh_armstrong(153))  # Saída: True
print(eh_armstrong(370))  # Saída: True
print(eh_armstrong(123))  # Saída: False


# 38. Crie uma função média_harmonica(lista) que calcula a média harmônica de uma lista de números.
def media_harmonica(lista):
    n = len(lista)
    soma_inversos = sum(1 / x for x in lista if x != 0)
    return n / soma_inversos if soma_inversos else 0

# Teste da função média_harmonica
print(media_harmonica([1, 2, 3, 4]))  # Saída: 1.92
print(media_harmonica([1, 0, 3]))  # Saída: 1.5


# 39. Implemente uma função aproxima_pi(n) que calcula uma aproximação do número pi usando n termos da série de Leibniz.
def aproxima_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi

# Teste da função aproxima_pi
print(aproxima_pi(1000))  # Saída aproximada de pi: 3.140592653839794
print(aproxima_pi(10000))  # Saída aproximada de pi: 3.141492653590034


# 40. Escreva uma função mediana(lista) que retorne a mediana de uma lista de números.
def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        return lista[n // 2]

# Teste da função mediana
print(mediana([1, 3, 2, 4, 5]))  # Saída: 3
print(mediana([1, 3, 2, 4]))  # Saída: 2.5

# 41. Implemente a função fibonacci(n) que retorna o n-ésimo termo da sequência de Fibonacci.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Teste
print(fibonacci(5))  # Saída: 5


# 42. Crie uma função soma_recursiva(n) que soma todos os números de 1 até n recursivamente.
def soma_recursiva(n):
    if n == 0:
        return 0
    return n + soma_recursiva(n-1)

# Teste
print(soma_recursiva(5))  # Saída: 15


# 43. Escreva uma função recursiva produto(a, b) que multiplica dois números inteiros a e b.
def produto(a, b):
    if b == 0:
        return 0
    return a + produto(a, b-1)

# Teste
print(produto(3, 4))  # Saída: 12


# 44. Implemente uma função potencia_recursiva(base, exp) que calcula a potência de forma recursiva.
def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    return base * potencia_recursiva(base, exp - 1)

# Teste
print(potencia_recursiva(2, 3))  # Saída: 8


# 45. Crie uma função somatorio_lista_recursivo(lista) que retorne a soma dos elementos de uma lista recursivamente.
def somatorio_lista_recursivo(lista):
    if not lista:
        return 0
    return lista[0] + somatorio_lista_recursivo(lista[1:])

# Teste
print(somatorio_lista_recursivo([1, 2, 3, 4, 5]))  # Saída: 15


# 46. Escreva uma função inverte_string_recursiva(s) que inverta uma string recursivamente.
def inverte_string_recursiva(s):
    if len(s) == 0:
        return s
    return inverte_string_recursiva(s[1:]) + s[0]

# Teste
print(inverte_string_recursiva("python"))  # Saída: nohtyp


# 47. Implemente uma função conta_ocorrencias_recursiva(lista, elem) que conte o número de ocorrências de um elemento em uma lista de forma recursiva.
def conta_ocorrencias_recursiva(lista, elem):
    if not lista:
        return 0
    return (1 if lista[0] == elem else 0) + conta_ocorrencias_recursiva(lista[1:], elem)

# Teste
print(conta_ocorrencias_recursiva([1, 2, 3, 1, 4], 1))  # Saída: 2


# 48. Crie uma função mcd(a, b) que calcule o máximo divisor comum de dois números usando recursão.
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

# Teste
print(mcd(48, 18))  # Saída: 6


# 49. Escreva uma função mdc_lista(lista) que retorne o maior divisor comum entre os números de uma lista.
def mdc_lista(lista):
    from functools import reduce
    return reduce(mcd, lista)

# Teste
print(mdc_lista([48, 18, 30]))  # Saída: 6


# 50. Implemente a função torre_hanoi(n, origem, destino, auxiliar) para resolver o problema da Torre de Hanói.
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover disco de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

# Teste
torre_hanoi(3, 'A', 'C', 'B')


# 51. Crie uma função verifica_ano_bissexto(ano) que retorna True se o ano for bissexto.
def verifica_ano_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

# Teste
print(verifica_ano_bissexto(2020))  # Saída: True


# 52. Escreva uma função soma_diagonais(matriz) que retorne a soma dos elementos das diagonais de uma matriz.
def soma_diagonais(matriz):
    diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonal_secundaria = sum(matriz[i][len(matriz)-i-1] for i in range(len(matriz)))
    return diagonal_principal + diagonal_secundaria

# Teste
print(soma_diagonais([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Saída: 25


# 53. Implemente uma função conta_ocorrencias_caracteres(s) que retorne um dicionário com a contagem de cada caractere em uma string.
def conta_ocorrencias_caracteres(s):
    return {char: s.count(char) for char in set(s)}

# Teste
print(conta_ocorrencias_caracteres("banana"))  # Saída: {'a': 3, 'n': 2, 'b': 1}


# 54. Crie uma função media_notas(dicionario) que recebe um dicionário de alunos e notas e retorna a média das notas.
def media_notas(dicionario):
    return sum(dicionario.values()) / len(dicionario)

# Teste
print(media_notas({'João': 8, 'Maria': 9, 'Pedro': 7}))  # Saída: 8.0


# 55. Escreva uma função converte_segundos(h, m, s) que converte horas, minutos e segundos em segundos.
def converte_segundos(h, m, s):
    return h * 3600 + m * 60 + s

# Teste
print(converte_segundos(1, 2, 3))  # Saída: 3723


# 56. Crie uma função gera_fibonacci_lista(n) que gera uma lista com os n primeiros números de Fibonacci.
def gera_fibonacci_lista(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Teste
print(gera_fibonacci_lista(5))  # Saída: [0, 1, 1, 2, 3]


# 57. Implemente uma função substitui_espaco(texto, simbolo) que substitua todos os espaços em uma string por um símbolo específico.
def substitui_espaco(texto, simbolo):
    return texto.replace(" ", simbolo)

# Teste
print(substitui_espaco("Olá Mundo", "-"))  # Saída: Olá-Mundo


# 58. Escreva uma função conta_maiusculas(texto) que conta o número de letras maiúsculas em um texto.
def conta_maiusculas(texto):
    return sum(1 for char in texto if char.isupper())

# Teste
print(conta_maiusculas("Python É Lindo"))  # Saída: 3


# 59. Crie uma função ordena_lista(lista) que retorne a lista ordenada em ordem crescente.
def ordena_lista(lista):
    return sorted(lista)

# Teste
print(ordena_lista([5, 3, 8, 1, 4]))  # Saída: [1, 3, 4, 5, 8]


# 60. Implemente uma função filtra_pares(lista) que retorne uma lista apenas com os números pares.
def filtra_pares(lista):
    return [x for x in lista if x % 2 == 0]

# Teste
print(filtra_pares([1, 2, 3, 4, 5, 6]))  # Saída: [2, 4, 6]

# 61. Crie uma função bubblesort(lista) que ordene uma lista usando o algoritmo Bubble Sort.
def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Teste para a função bubblesort
def test_bubblesort():
    assert bubblesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bubblesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubblesort([1]) == [1]
    print("test_bubblesort passou!")

# 62. Implemente uma função valida_senha(senha) que verifique se uma senha atende a requisitos (tamanho, caracteres especiais, etc.).
def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in "!@#$%^&*()_+" for c in senha):
        return False
    return True

# Teste para a função valida_senha
def test_valida_senha():
    assert valida_senha("Senha123!") == True
    assert valida_senha("senha123") == False
    assert valida_senha("12345678") == False
    assert valida_senha("Senha") == False
    print("test_valida_senha passou!")

# 63. Escreva uma função calcula_juros_compostos(capital, taxa, tempo) que retorne o montante final.
def calcula_juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

# Teste para a função calcula_juros_compostos
def test_calcula_juros_compostos():
    assert calcula_juros_compostos(1000, 0.05, 2) == 1102.5
    assert calcula_juros_compostos(500, 0.1, 3) == 665.5
    assert calcula_juros_compostos(100, 0.2, 1) == 120.0
    print("test_calcula_juros_compostos passou!")

# 64. Crie uma função gera_senha(tamanho) que gere uma senha aleatória de um tamanho específico.
import random
import string

def gera_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Teste para a função gera_senha
def test_gera_senha():
    senha = gera_senha(10)
    assert len(senha) == 10
    assert any(c.isdigit() for c in senha)
    assert any(c.isupper() for c in senha)
    print("test_gera_senha passou!")

# 65. Implemente uma função dec2bin(n) que converte um número decimal para binário.
def dec2bin(n):
    return bin(n)[2:]

# Teste para a função dec2bin
def test_dec2bin():
    assert dec2bin(10) == "1010"
    assert dec2bin(0) == "0"
    assert dec2bin(255) == "11111111"
    print("test_dec2bin passou!")

# 66. Escreva uma função bin2dec(binario) que converte um número binário para decimal.
def bin2dec(binario):
    return int(binario, 2)

# Teste para a função bin2dec
def test_bin2dec():
    assert bin2dec("1010") == 10
    assert bin2dec("0") == 0
    assert bin2dec("11111111") == 255
    print("test_bin2dec passou!")

# 67. Crie uma função valida_email(email) que verifique se um e-mail é válido.
import re

def valida_email(email):
    padrao = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(padrao, email))

# Teste para a função valida_email
def test_valida_email():
    assert valida_email("teste@exemplo.com") == True
    assert valida_email("testeexemplo.com") == False
    assert valida_email("test@com") == False
    print("test_valida_email passou!")

# 68. Implemente uma função tamanho_arquivo(nome_arquivo) que retorne o tamanho de um arquivo em bytes.
import os

def tamanho_arquivo(nome_arquivo):
    return os.path.getsize(nome_arquivo)

# Teste para a função tamanho_arquivo
def test_tamanho_arquivo():
    with open('teste.txt', 'w') as f:
        f.write("Este é um arquivo de teste.")
    assert tamanho_arquivo('teste.txt') == 22
    os.remove('teste.txt')
    print("test_tamanho_arquivo passou!")

# 69. Escreva uma função minimax(lista) que retorne o menor e o maior número de uma lista.
def minimax(lista):
    return min(lista), max(lista)

# Teste para a função minimax
def test_minimax():
    assert minimax([1, 2, 3, 4, 5]) == (1, 5)
    assert minimax([5, 4, 3, 2, 1]) == (1, 5)
    assert minimax([7]) == (7, 7)
    print("test_minimax passou!")

# 70. Crie uma função classifica_triangulo(a, b, c) que classifique um triângulo com base em seus lados.
def classifica_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

# Teste para a função classifica_triangulo
def test_classifica_triangulo():
    assert classifica_triangulo(3, 3, 3) == "Equilátero"
    assert classifica_triangulo(3, 3, 4) == "Isósceles"
    assert classifica_triangulo(3, 4, 5) == "Escaleno"
    print("test_classifica_triangulo passou!")

# 71. Crie uma função conta_elementos(lista) que retorne um dicionário com a contagem de cada elemento na lista.
from collections import Counter

def conta_elementos(lista):
    return dict(Counter(lista))

# Teste para a função conta_elementos
def test_conta_elementos():
    assert conta_elementos([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert conta_elementos(['a', 'b', 'b', 'c', 'c', 'c']) == {'a': 1, 'b': 2, 'c': 3}
    assert conta_elementos([1]) == {1: 1}
    print("test_conta_elementos passou!")

# 72. Escreva uma função merge_dicionarios(d1, d2) que una dois dicionários, somando os valores das chaves iguais.
def merge_dicionarios(d1, d2):
    resultado = d1.copy()  # Faz uma cópia do primeiro dicionário
    for chave, valor in d2.items():
        resultado[chave] = resultado.get(chave, 0) + valor
    return resultado

# Teste para a função merge_dicionarios
def test_merge_dicionarios():
    assert merge_dicionarios({'a': 1, 'b': 2}, {'a': 3, 'c': 4}) == {'a': 4, 'b': 2, 'c': 4}
    assert merge_dicionarios({'x': 5}, {'x': 1, 'y': 2}) == {'x': 6, 'y': 2}
    assert merge_dicionarios({}, {}) == {}
    print("test_merge_dicionarios passou!")

# 73. Implemente uma função filtro_dicionario(dic, valor) que retorne um novo dicionário apenas com as chaves onde os valores são maiores que valor.
def filtro_dicionario(dic, valor):
    return {k: v for k, v in dic.items() if v > valor}

# Teste para a função filtro_dicionario
def test_filtro_dicionario():
    assert filtro_dicionario({'a': 1, 'b': 3, 'c': 2}, 2) == {'b': 3}
    assert filtro_dicionario({'x': 5, 'y': 1, 'z': 4}, 3) == {'x': 5, 'z': 4}
    assert filtro_dicionario({'a': 1, 'b': 1}, 1) == {}
    print("test_filtro_dicionario passou!")

# 74. Crie uma função ordena_por_valores(dic) que ordene um dicionário por seus valores e retorne o resultado.
def ordena_por_valores(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1]))

# Teste para a função ordena_por_valores
def test_ordena_por_valores():
    assert ordena_por_valores({'a': 3, 'b': 1, 'c': 2}) == {'b': 1, 'c': 2, 'a': 3}
    assert ordena_por_valores({'x': 5, 'y': 2, 'z': 4}) == {'y': 2, 'z': 4, 'x': 5}
    assert ordena_por_valores({'a': 1}) == {'a': 1}
    print("test_ordena_por_valores passou!")

# 75. Escreva uma função inverte_dicionario(dic) que inverta as chaves e valores de um dicionário.
def inverte_dicionario(dic):
    return {v: k for k, v in dic.items()}

# Teste para a função inverte_dicionario
def test_inverte_dicionario():
    assert inverte_dicionario({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
    assert inverte_dicionario({'x': 5, 'y': 10}) == {5: 'x', 10: 'y'}
    assert inverte_dicionario({'a': 'x', 'b': 'y'}) == {'x': 'a', 'y': 'b'}
    print("test_inverte_dicionario passou!")

# 76. Implemente uma função escreve_arquivo(nome_arquivo, texto) que crie um arquivo com um texto.
def escreve_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as f:
        f.write(texto)

# Teste para a função escreve_arquivo
def test_escreve_arquivo():
    escreve_arquivo('arquivo_teste.txt', 'Olá, Mundo!')
    with open('arquivo_teste.txt', 'r') as f:
        assert f.read() == 'Olá, Mundo!'
    print("test_escreve_arquivo passou!")

# 77. Crie uma função le_arquivo(nome_arquivo) que leia o conteúdo de um arquivo e retorne uma string.
def le_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return f.read()

# Teste para a função le_arquivo
def test_le_arquivo():
    escreve_arquivo('arquivo_teste.txt', 'Conteúdo do arquivo')
    assert le_arquivo('arquivo_teste.txt') == 'Conteúdo do arquivo'
    print("test_le_arquivo passou!")

# 78. Escreva uma função conta_linhas(nome_arquivo) que retorne o número de linhas de um arquivo.
def conta_linhas(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.readlines())

# Teste para a função conta_linhas
def test_conta_linhas():
    escreve_arquivo('arquivo_linhas.txt', 'Linha 1\nLinha 2\nLinha 3\n')
    assert conta_linhas('arquivo_linhas.txt') == 3
    print("test_conta_linhas passou!")

# 79. Implemente uma função conta_palavras_arquivo(nome_arquivo) que retorne o número total de palavras em um arquivo.
def conta_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return len(f.read().split())

# Teste para a função conta_palavras_arquivo
def test_conta_palavras_arquivo():
    escreve_arquivo('arquivo_palavras.txt', 'Este é um arquivo com várias palavras.')
    assert conta_palavras_arquivo('arquivo_palavras.txt') == 7
    print("test_conta_palavras_arquivo passou!")

# 80. Crie uma função substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova) que substitua todas as ocorrências de uma palavra em um arquivo por outra.
def substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
    conteudo = conteudo.replace(palavra_antiga, palavra_nova)
    with open(nome_arquivo, 'w') as f:
        f.write(conteudo)

# Teste para a função substitui_texto_arquivo
def test_substitui_texto_arquivo():
    escreve_arquivo('arquivo_substitui.txt', 'Eu gosto de maçã.')
    substitui_texto_arquivo('arquivo_substitui.txt', 'maçã', 'banana')
    assert le_arquivo('arquivo_substitui.txt') == 'Eu gosto de banana.'
    print("test_substitui_texto_arquivo passou!")

# 81. Crie uma função data_atual() que retorne a data atual no formato "dd/mm/aaaa".
from datetime import datetime

def data_atual():
    return datetime.now().strftime("%d/%m/%Y")

# Teste para a função data_atual
def test_data_atual():
    assert data_atual() == datetime.now().strftime("%d/%m/%Y")
    print("test_data_atual passou!")

# 82. Escreva uma função dias_entre_datas(data1, data2) que retorne a diferença em dias entre duas datas.
from datetime import datetime

def dias_entre_datas(data1, data2):
    data1 = datetime.strptime(data1, "%d/%m/%Y")
    data2 = datetime.strptime(data2, "%d/%m/%Y")
    return abs((data2 - data1).days)

# Teste para a função dias_entre_datas
def test_dias_entre_datas():
    assert dias_entre_datas("01/01/2024", "10/01/2024") == 9
    assert dias_entre_datas("10/01/2024", "01/01/2024") == 9
    assert dias_entre_datas("01/01/2024", "01/01/2024") == 0
    print("test_dias_entre_datas passou!")

# 83. Implemente uma função adiciona_dias(data, n) que adicione n dias a uma data e retorne o novo valor.
from datetime import datetime, timedelta

def adiciona_dias(data, n):
    data = datetime.strptime(data, "%d/%m/%Y")
    nova_data = data + timedelta(days=n)
    return nova_data.strftime("%d/%m/%Y")

# Teste para a função adiciona_dias
def test_adiciona_dias():
    assert adiciona_dias("01/01/2024", 10) == "11/01/2024"
    assert adiciona_dias("31/12/2024", 1) == "01/01/2025"
    assert adiciona_dias("01/01/2024", 0) == "01/01/2024"
    print("test_adiciona_dias passou!")

# 84. Crie uma função formato_12h_para_24h(hora_12h) que converta uma hora no formato 12h para 24h.
from datetime import datetime

def formato_12h_para_24h(hora_12h):
    return datetime.strptime(hora_12h, "%I:%M %p").strftime("%H:%M")

# Teste para a função formato_12h_para_24h
def test_formato_12h_para_24h():
    assert formato_12h_para_24h("02:30 PM") == "14:30"
    assert formato_12h_para_24h("12:00 AM") == "00:00"
    assert formato_12h_para_24h("01:45 AM") == "01:45"
    print("test_formato_12h_para_24h passou!")

# 85. Escreva uma função formato_24h_para_12h(hora_24h) que converta uma hora no formato 24h para 12h.
from datetime import datetime

def formato_24h_para_12h(hora_24h):
    return datetime.strptime(hora_24h, "%H:%M").strftime("%I:%M %p")

# Teste para a função formato_24h_para_12h
def test_formato_24h_para_12h():
    assert formato_24h_para_12h("14:30") == "02:30 PM"
    assert formato_24h_para_12h("00:00") == "12:00 AM"
    assert formato_24h_para_12h("01:45") == "01:45 AM"
    print("test_formato_24h_para_12h passou!")

# 86. Crie uma função geradora conta_ate_n(n) que gere números de 1 até n.
def conta_ate_n(n):
    for i in range(1, n + 1):
        yield i

# Teste para a função conta_ate_n
def test_conta_ate_n():
    assert list(conta_ate_n(5)) == [1, 2, 3, 4, 5]
    assert list(conta_ate_n(3)) == [1, 2, 3]
    assert list(conta_ate_n(1)) == [1]
    print("test_conta_ate_n passou!")

# 87. Implemente um gerador pares(n) que gere todos os números pares de 1 até n.
def pares(n):
    for i in range(2, n + 1, 2):
        yield i

# Teste para a função pares
def test_pares():
    assert list(pares(10)) == [2, 4, 6, 8, 10]
    assert list(pares(5)) == [2, 4]
    assert list(pares(2)) == [2]
    print("test_pares passou!")

# 88. Escreva um gerador quadrados(n) que gere os quadrados dos números de 1 até n.
def quadrados(n):
    for i in range(1, n + 1):
        yield i ** 2

# Teste para a função quadrados
def test_quadrados():
    assert list(quadrados(5)) == [1, 4, 9, 16, 25]
    assert list(quadrados(3)) == [1, 4, 9]
    assert list(quadrados(1)) == [1]
    print("test_quadrados passou!")

# 89. Crie um gerador fibonacci_gen(n) que gere os primeiros n termos da sequência de Fibonacci.
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Teste para a função fibonacci_gen
def test_fibonacci_gen():
    assert list(fibonacci_gen(5)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_gen(3)) == [0, 1, 1]
    assert list(fibonacci_gen(1)) == [0]
    print("test_fibonacci_gen passou!")
