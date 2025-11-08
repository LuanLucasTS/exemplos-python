def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

if __name__ == "__main__":
    print("Calculadora simples")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    if operacao == '+':
        print("Resultado:", soma(a, b))
    elif operacao == '-':
        print("Resultado:", subtracao(a, b))
    elif operacao == '*':
        print("Resultado:", multiplicacao(a, b))
    elif operacao == '/':
        print("Resultado:", divisao(a, b))
    else:
        print("Operação inválida.")
