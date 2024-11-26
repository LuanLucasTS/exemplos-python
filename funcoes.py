#1.	Multiplicação Escalar em Lista: Crie uma função multiplica_escalar(lista, escalar) que recebe uma lista de números e um escalar, e multiplica cada elemento da lista pelo escalar, retornando a nova lista.
def multiplica_escalar(lista, escalar):
    return [elemento * escalar for elemento in lista]

numeros = [1, 2, 3, 4]
escalar = 3
resultado = multiplica_escalar(numeros, escalar)
print(resultado)  # Saída: [3, 6, 9, 12]

#2.	Produto de uma Lista: Escreva uma função produto_lista(lista) que calcula o produto (multiplicação) de todos os elementos de uma lista.
def produto_lista(lista):
    produto = 1
    for elemento in lista:
        produto *= elemento
    return produto
numeros = [2, 3, 4]
resultado = produto_lista(numeros)
print(resultado)  # Saída: 24

#3.	Conta Consoantes: Implemente uma função conta_consoantes(texto) que conta o número de consoantes em uma string.
def conta_consoantes(texto):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for letra in texto:
        if letra in consoantes:
            contador += 1
    return contador
texto = "Olá, Mundo!"
resultado = conta_consoantes(texto)
print(resultado)  # Saída: 5

#4.	Concatenação de Listas: Crie uma função concatena_listas(lista1, lista2) que recebe duas listas e retorna uma nova lista com os elementos de ambas as listas concatenados.
def concatena_listas(lista1, lista2):
    return lista1 + lista2
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = concatena_listas(lista1, lista2)
print(resultado)  # Saída: [1, 2, 3, 4, 5, 6]

#5.	Soma dos N primeiros Naturais: Escreva uma função soma_naturais(n) que retorna a soma dos N primeiros números naturais.
def soma_naturais(n):
    return n * (n + 1) // 2
n = 5
resultado = soma_naturais(n)
print(resultado)  # Saída: 15 (1 + 2 + 3 + 4 + 5)

#6.	Diferença de Conjuntos: Implemente uma função diferenca_conjuntos(lista1, lista2) que retorna os elementos presentes em lista1 que não estão em lista2.
def diferenca_conjuntos(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
resultado = diferenca_conjuntos(lista1, lista2)
print(resultado)  # Saída: [1, 2]

#7.	Ordenação com Selection Sort: Crie uma função selection_sort(lista) que ordena uma lista usando o algoritmo de Selection Sort.
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontra o índice do menor elemento a partir de i
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        # Troca o elemento atual com o menor elemento encontrado
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
numeros = [64, 25, 12, 22, 11]
resultado = selection_sort(numeros)
print(resultado)  # Saída: [11, 12, 22, 25, 64]

#8.	Ordenação com Insertion Sort: Implemente uma função insertion_sort(lista) que ordena uma lista usando o algoritmo de Insertion Sort.
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        # Move os elementos da lista que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista
numeros = [12, 11, 13, 5, 6]
resultado = insertion_sort(numeros)
print(resultado)  # Saída: [5, 6, 11, 12, 13]

#9.	Ordenação com Quick Sort: Escreva uma função quick_sort(lista) que ordena uma lista usando o algoritmo de Quick Sort (versão não recursiva).
def quick_sort(lista):
    # Cria uma pilha para armazenar os índices dos subarrays
    pilha = [(0, len(lista) - 1)]

    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:
            # Particiona o subarray e obtém o índice do pivô
            piv = partition(lista, inicio, fim)
            # Adiciona as partes do subarray à pilha
            pilha.append((inicio, piv - 1))
            pilha.append((piv + 1, fim))
    return lista

def partition(lista, inicio, fim):
    # Escolhe o último elemento como pivô
    piv = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if lista[j] < piv:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
numeros = [10, 7, 8, 9, 1, 5]
resultado = quick_sort(numeros)
print(resultado)  # Saída: [1, 5, 7, 8, 9, 10]

#10.	Diferença entre Máximo e Mínimo: Crie uma função diferenca_max_min(lista) que retorna a diferença entre o maior e o menor elemento de uma lista.
def diferenca_max_min(lista):
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia
    return max(lista) - min(lista)
numeros = [10, 7, 8, 9, 1, 5]
resultado = diferenca_max_min(numeros)
print(resultado)  # Saída: 9 (10 - 1)

#11.	Produto Escalar entre Vetores: Implemente uma função produto_escalar(vetor1, vetor2) que retorna o produto escalar entre dois vetores (listas de números) de mesmo tamanho.
def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")

    produto = sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))
    return produto
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_escalar(vetor1, vetor2)
print(resultado)  # Saída: 32 (1*4 + 2*5 + 3*6)

#12.	Listas Pares e Ímpares: Escreva uma função separa_pares_impares(lista) que separa uma lista de números em duas listas: uma com os pares e outra com os ímpares.
def separa_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares, impares = separa_pares_impares(numeros)
print("Pares:", pares)    # Saída: [2, 4, 6, 8]
print("Ímpares:", impares)  # Saída: [1, 3, 5, 7]

#13.	Diferença Absoluta entre Elementos de Lista: Crie uma função diferença_elementos_lista(lista) que retorna uma lista com a diferença absoluta entre cada par consecutivo de elementos da lista original.
def diferenca_elementos_lista(lista):
    return [abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1)]
numeros = [10, 7, 3, 15]
resultado = diferenca_elementos_lista(numeros)
print(resultado)  # Saída: [3, 4, 12]

#14.	Desvio Padrão de Lista: Implemente uma função desvio_padrao(lista) que calcula o desvio padrão dos elementos em uma lista de números.
import math

def desvio_padrao(lista):
    if len(lista) < 2:
        raise ValueError("A lista deve ter pelo menos dois elementos")

    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)
numeros = [10, 12, 23, 23, 16, 23, 21, 16]
resultado = desvio_padrao(numeros)
print(resultado)  # Saída: 4.898979485566356

#15.	Multiplicação de Matrizes 2x2: Crie uma função multiplica_matrizes(matriz1, matriz2) que recebe duas matrizes 2x2 e retorna o resultado da multiplicação entre elas.
def multiplica_matrizes(matriz1, matriz2):
    # Verifica se ambas as matrizes são 2x2
    if len(matriz1) != 2 or len(matriz2) != 2 or len(matriz1[0]) != 2 or len(matriz2[0]) != 2:
        raise ValueError("Ambas as matrizes devem ser 2x2")

    # Multiplicação das matrizes 2x2
    resultado = [
        [
            matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],  # Linha 1, Coluna 1
            matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]   # Linha 1, Coluna 2
        ],
        [
            matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],  # Linha 2, Coluna 1
            matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]   # Linha 2, Coluna 2
        ]
    ]
    return resultado
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplica_matrizes(matriz1, matriz2)
print(resultado)
# Saída: [[19, 22], [43, 50]]

#16.	Busca Binária: Implemente uma função busca_binaria(lista, elemento) que realiza uma busca binária em uma lista ordenada e retorna o índice do elemento, ou -1 se não for encontrado.
def busca_binaria(lista, elemento):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio  # Retorna o índice do elemento encontrado
        elif lista[meio] < elemento:
            inicio = meio + 1  # Elemento está na metade direita
        else:
            fim = meio - 1  # Elemento está na metade esquerda

    return -1  # Retorna -1 se o elemento não for encontrado
lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento = 7
resultado = busca_binaria(lista, elemento)
print(resultado)  # Saída: 3 (índice do elemento 7)

#17.	Intercala Listas Ordenadas: Crie uma função intercala_listas_ordenadas(lista1, lista2) que recebe duas listas ordenadas e retorna uma nova lista intercalada e ordenada.
def intercala_listas_ordenadas(lista1, lista2):
    resultado = []
    i, j = 0, 0

    # Enquanto ambos os índices forem válidos
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Adiciona o restante dos elementos de lista1 ou lista2, se houver
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
resultado = intercala_listas_ordenadas(lista1, lista2)
print(resultado)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8]

#18.	Média Ponderada: Escreva uma função media_ponderada(lista_valores, lista_pesos) que calcula a média ponderada de uma lista de valores com uma lista de pesos correspondente.
def media_ponderada(lista_valores, lista_pesos):
    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    soma_valores_pesos = sum(valor * peso for valor, peso in zip(lista_valores, lista_pesos))
    soma_pesos = sum(lista_pesos)

    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    return soma_valores_pesos / soma_pesos
valores = [10, 8, 7, 9]
pesos = [2, 1, 3, 4]
resultado = media_ponderada(valores, pesos)
print(resultado)  # Saída: 8.25

#19.	Diagonais de uma Matriz: Implemente uma função diagonais_matriz(matriz) que recebe uma matriz quadrada e retorna uma lista contendo os elementos das duas diagonais.
def diagonais_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz deve ser quadrada.")

    diagonal_principal = []
    diagonal_secundaria = []
    n = len(matriz)

    for i in range(n):
        diagonal_principal.append(matriz[i][i])  # Elementos da diagonal principal
        diagonal_secundaria.append(matriz[i][n-i-1])  # Elementos da diagonal secundária

    return diagonal_principal, diagonal_secundaria
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonais = diagonais_matriz(matriz)
print(diagonais)  # Saída: ([1, 5, 9], [3, 5, 7])

#20.	Conta Números em Intervalo: Crie uma função conta_intervalo(lista, inicio, fim) que conta quantos números em uma lista estão dentro de um intervalo [inicio, fim].
def conta_intervalo(lista, inicio, fim):
    contador = 0
    for numero in lista:
        if inicio <= numero <= fim:
            contador += 1
    return contador
lista = [1, 3, 5, 7, 9, 11, 13]
inicio = 5
fim = 10
resultado = conta_intervalo(lista, inicio, fim)
print(resultado)  # Saída: 4 (números dentro do intervalo: 5, 7, 9, 10)

#21.	Converte Celsius para Fahrenheit: Escreva uma função celsius_para_fahrenheit(celsius) que converte uma temperatura em Celsius para Fahrenheit.
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(temperatura_fahrenheit)  # Saída: 77.0

#22.	Converte Fahrenheit para Celsius: Crie uma função fahrenheit_para_celsius(fahrenheit) que converte uma temperatura em Fahrenheit para Celsius.
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperatura_fahrenheit = 77
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(temperatura_celsius)  # Saída: 25.0

#23.	Multiplicação de Valores Pares: Implemente uma função multiplica_pares(lista) que multiplica todos os números pares em uma lista.
def multiplica_pares(lista):
    resultado = 1
    encontrou_par = False  # Variável para verificar se encontrou algum número par

    for numero in lista:
        if numero % 2 == 0:  # Verifica se o número é par
            resultado *= numero
            encontrou_par = True

    # Se não encontrou nenhum número par, retorna 0
    if not encontrou_par:
        return 0

    return resultado
lista = [1, 2, 3, 4, 5, 6]
resultado = multiplica_pares(lista)
print(resultado)  # Saída: 48 (2 * 4 * 6)

#24.	Números Primos até N: Escreva uma função numeros_primos(n) que retorna uma lista de todos os números primos até um número n dado.
def numeros_primos(n):
    primos = []

    for numero in range(2, n+1):  # Começa de 2, pois 1 não é primo
        is_primo = True
        for i in range(2, int(numero ** 0.5) + 1):  # Testa até a raiz quadrada de 'numero'
            if numero % i == 0:  # Se 'numero' for divisível por 'i', não é primo
                is_primo = False
                break
        if is_primo:
            primos.append(numero)

    return primos
n = 20
primos = numeros_primos(n)
print(primos)  # Saída: [2, 3, 5, 7, 11, 13, 17, 19]

#25.	Concatenação de Strings: Crie uma função concatena_strings(lista_strings) que recebe uma lista de strings e retorna uma única string com todas as strings concatenadas.
def concatena_strings(lista_strings):
    return ''.join(lista_strings)
lista = ["Olá", " ", "mundo", "!", " ", "Como", " ", "vai?"]
resultado = concatena_strings(lista)
print(resultado)  # Saída: "Olá mundo! Como vai?"

#26.	Ordenação com Merge Sort: Implemente uma função merge_sort(lista) que ordena uma lista usando o algoritmo de Merge Sort.
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Ordena recursivamente as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Junta as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Combina as duas listas ordenadas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes, se houver
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
lista = [34, 7, 23, 32, 5, 62]
resultado = merge_sort(lista)
print(resultado)  # Saída: [5, 7, 23, 32, 34, 62]

#27.	Verifica Ordem Crescente: Crie uma função esta_ordenada(lista) que verifica se uma lista está ordenada em ordem crescente.
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:  # Se o elemento atual for maior que o próximo, a lista não está ordenada
            return False
    return True
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 4, 5]

print(esta_ordenada(lista1))  # Saída: True
print(esta_ordenada(lista2))  # Saída: False

#28.	Remove Múltiplos de um Número: Escreva uma função remove_multiplos(lista, n) que remove todos os múltiplos de n de uma lista.
def remove_multiplos(lista, n):
    return [x for x in lista if x % n != 0]
lista = [10, 15, 20, 25, 30, 35]
n = 5
resultado = remove_multiplos(lista, n)
print(resultado)  # Saída: [25, 35]

#29.	Intervalo entre Elementos de uma Lista: Implemente uma função intervalo_entre_elementos(lista) que calcula o intervalo (diferença) entre o maior e o menor valor de uma lista.
def intervalo_entre_elementos(lista):
    if not lista:  # Verifica se a lista está vazia
        return 0
    return max(lista) - min(lista)
lista = [10, 20, 5, 30, 25]
resultado = intervalo_entre_elementos(lista)
print(resultado)  # Saída: 25

#30.	Histograma de Ocorrências em Lista: Crie uma função histograma(lista) que recebe uma lista e retorna um dicionário com o número de ocorrências de cada elemento da lista.
def histograma(lista):
    ocorrencias = {}
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1  # Incrementa o contador se o item já estiver no dicionário
        else:
            ocorrencias[item] = 1  # Adiciona o item ao dicionário com contador 1
    return ocorrências
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = histograma(lista)
print(resultado)  # Saída: {1: 1, 2: 2, 3: 3, 4: 4}
