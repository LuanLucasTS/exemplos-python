# 1 Crie uma classe Pessoa com os atributos nome e idade. Instancie um objeto e imprima suas informações.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Imprimindo as informações da pessoa
pessoa1.exibir_informacoes()


# 2 Crie uma classe Retângulo com os atributos largura e altura. Adicione um método para calcular a área.
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Criando uma instância da classe Retangulo
retangulo1 = Retangulo(5, 3)

# Calculando e exibindo a área do retângulo
area = retangulo1.calcular_area()
print(f"A área do retângulo é: {area}")
# 3 Crie uma classe Carro com os atributos marca e ano. Adicione um método que exiba essas informações.
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}")

# Criando uma instância da classe Carro
carro1 = Carro("Toyota", 2020)

# Exibindo as informações do carro
carro1.exibir_informacoes()


# 4 Crie uma classe Livro com os atributos titulo e autor. Adicione um método para exibir os detalhes do livro.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

# Criando uma instância da classe Livro
livro1 = Livro("1984", "George Orwell")

# Exibindo os detalhes do livro
livro1.exibir_detalhes()


# 5 Crie uma classe Circulo com um atributo raio. Adicione um método para calcular o perímetro (2πr).
import math

class Circulo:
  def __init__(self, raio):
    self.raio = raio

  def calcular_perimetro(self):
    return 2 * math.pi * self.raio

# Criando um objeto da classe Circulo
circulo1 = Circulo(5)

# Calculando e imprimindo o perímetro
perimetro = circulo1.calcular_perimetro()
print("O perímetro do círculo é:", perimetro)


# 6 Crie uma classe Animal com os atributos espécie e som. Adicione um método que  imprima o som do animal. 
class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f"O {self.especie} faz {self.som}")

# Exemplos de uso:
cachorro = Animal("cachorro", "au au")
gato = Animal("gato", "miau")
passaro = Animal("pássaro", "pio pio")

cachorro.emitir_som()  # Saída: O cachorro faz au au
gato.emitir_som()     # Saída: O gato faz miau
passaro.emitir_som()  # Saída: O pássaro faz pio pio


# 7 Crie uma classe Produto com os atributos nome e preço. Adicione um método para aplicar um desconto ao preço. 
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

# Exemplo de uso:
produto1 = Produto("Camiseta", 50.0)
produto1.aplicar_desconto(20)  # Aplica um desconto de 20%
print(f"O preço do {produto1.nome} com desconto é R$ {produto1.preco:.2f}")


# 8 Crie uma classe Calculadora com métodos para somar e subtrair dois números.
class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2


# Exemplo de uso:
calculadora = Calculadora()
resultado_soma = calculadora.somar(5, 3)
resultado_subtracao = calculadora.subtrair(10, 4)

print("A soma é:", resultado_soma)
print("A subtração é:", resultado_subtracao)


# 9 Crie uma classe Aluno com atributos nome e nota. Adicione um método que exiba se o aluno está aprovado (nota >= 7).


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        if self.nota >= 7:
            print(f"{self.nome} está aprovado!")
        else:
            print(f"{self.nome} está reprovado!")

# Exemplo de uso:
aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 6.0)

aluno1.aprovado()  # Saída: João está aprovado!
aluno2.aprovado()  # Saída: Maria está reprovado!


# 10 Crie uma classe Temperatura com um método para converter graus Celsius para Fahrenheit.
class Temperatura:
    def celsius_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

# Exemplo de uso:
temperatura = Temperatura()
celsius = 30
fahrenheit = temperatura.celsius_para_fahrenheit(celsius)
print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")


# 11 Crie uma classe ContaBancaria com os atributos saldo. Adicione métodos para depositar e sacar dinheiro.
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")

# Exemplo de uso:
conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(1500)  # Tentativa de saque acima do saldo


# 12 Crie uma classe Filme com os atributos titulo e duracao. Adicione um método para exibir os detalhes.
class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao} minutos")

# Exemplo de uso:
filme1 = Filme("O Poderoso Chefão", 175)
filme2 = Filme("O Senhor dos Anéis: A Sociedade do Anel", 178)

filme1.exibir_detalhes()
filme2.exibir_detalhes()


# 13 Crie uma classe Veiculo com atributos modelo e velocidade. Adicione um método para aumentar a velocidade.
class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"O {self.modelo} está a {self.velocidade} km/h.")

# Exemplo de uso:
carro = Veiculo("Gol")
carro.acelerar(20)
carro.acelerar(30)


# 14 Crie uma classe Eletrodomestico com os atributos nome e potencia. Adicione um método para ligar o aparelho
class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.nome} foi ligado!")
        else:
            print(f"O {self.nome} já está ligado.")

# Exemplo de uso:
geladeira = Eletrodomestico("Geladeira", 150)
geladeira.ligar()
geladeira.ligar()  # Tentativa de ligar novamente


# 15 Crie uma classe Pessoa com um método para cumprimentar outra pessoa (imprimir "Olá, [nome]").
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa):
        print(f"Olá, {outra_pessoa.nome}!")

# Exemplo de uso:
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

pessoa1.cumprimentar(pessoa2)  # Imprime: Olá, Maria!


# 16 Crie uma classe Pessoa com um método para cumprimentar outra pessoa (imprimir "Olá, [nome]").
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa):
        print(f"Olá, {outra_pessoa.nome}!")

# Exemplo de uso:
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

pessoa1.cumprimentar(pessoa2)  # Imprime: Olá, Maria!


# 17 Crie uma classe Data com os atributos dia, mes e ano. Adicione um método para formatar a data no estilo DD/MM/AAAA.
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

# Exemplo de uso:
data_nascimento = Data(15, 3, 1990)
print(data_nascimento.formatar())  # Saída: 15/03/1990


# 18 Crie uma classe Relogio com os atributos hora, minuto e segundo. Adicione um método para exibir o horário no formato HH:MM
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        print(f"{self.hora:02d}:{self.minuto:02d}")

# Exemplo de uso:
relogio = Relogio(15, 30, 25)
relogio.exibir_horario()  # Saída: 15:30

# 19 Crie uma classe ConversorMoeda com um método para converter dólares para reais.
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        print(f"{self.hora:02d}:{self.minuto:02d}")

# Exemplo de uso:
relogio = Relogio(15, 30, 25)
relogio.exibir_horario()  # Saída: 15:30


# 20 Crie uma classe Pessoa que inclua o atributo altura. Adicione um método para verificar se a pessoa é mais alta que 1,75 m.
class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def e_alta(self):
        return self.altura > 1.75

# Exemplo de uso:
pessoa1 = Pessoa("João", 1.80)
pessoa2 = Pessoa("Ana", 1.65)

print(f"{pessoa1.nome} é mais alta que 1,75m? {pessoa1.e_alta()}")
print(f"{pessoa2.nome} é mais alta que 1,75m? {pessoa2.e_alta()}")


# 21 Adicione à classe Livro um atributo para controlar a quantidade em estoque.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, quantidade_estoque):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.quantidade_estoque = quantidade_estoque

    def verificar_disponibilidade(self):
        if self.quantidade_estoque > 0:
            return "Livro disponível em estoque."
        else:
            return "Livro indisponível no momento."

# Exemplo de uso:
livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 10)
print(livro1.verificar_disponibilidade())  # Saída: Livro disponível em estoque.

livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, 0)
print(livro2.verificar_disponibilidade())  # Saída: Livro indisponível no momento.


# 22 Crie uma classe Agenda com um atributo para armazenar contatos e métodos para adicionar e listar contatos.
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = {
            'nome': nome,
            'telefone': telefone,
            'email': email
        }
        self.contatos.append(novo_contato)
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Sua 1  agenda está vazia.")
        else:
            print("Lista de contatos:")
            for contato in self.contatos:
                print(f"Nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")
                print("-" * 20)

# Exemplo de uso:
minha_agenda = Agenda()
minha_agenda.adicionar_contato("João Silva", "123456789", "joao@email.com")
minha_agenda.adicionar_contato("Maria Santos", "987654321", "maria@email.com")
minha_agenda.listar_contatos()


# 23 Crie uma classe Funcionario com os atributos nome e salario. Adicione um método para calcular um aumento de salário.
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Novo salário de {self.nome}: R${self.salario:.2f}")

# Exemplo de uso:
funcionario1 = Funcionario("João Silva", 2500)
funcionario1.calcular_aumento(10)  # Aumenta o salário em 10%


# 24 Crie uma classe Elevador com atributos andarAtual e totalAndares. Adicione métodos para subir e descer.
class Elevador:
    def __init__(self, total_andares):
        self.andar_atual = 0  # O elevador começa no térreo (andar 0).
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Subindo... Andar atual: {self.andar_atual}")
        else:
            print("Você já está no último andar.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Descendo... Andar atual: {self.andar_atual}")
        else:
            print("Você já está no térreo.")

# Exemplo de uso
elevador = Elevador(total_andares=10)
elevador.subir()  # Deve subir para o andar 1
elevador.subir()  # Deve subir para o andar 2
elevador.descer()  # Deve descer para o andar 1
elevador.descer()  # Deve descer para o térreo
elevador.descer()  # Deve exibir que já está no térreo


# 25 Crie uma classe Pessoa com atributos altura e peso. Adicione um método para calcular o IMC (peso / altura²).
class Pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

# Exemplo de uso:
pessoa1 = Pessoa(1.75, 70)
imc_pessoa1 = pessoa1.calcular_imc()
print(f"O IMC de pessoa1 é: {imc_pessoa1:.2f}")


# 26 Crie uma classe Calculadora com um histórico de operações realizadas.
class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, num1, num2):
        resultado = num1 + num2
        self.historico.append(f"{num1} + {num2} = {resultado}")
        return resultado

    def subtrair(self, num1, num2):
        resultado = num1 - num2
        self.historico.append(f"{num1} - {num2} = {resultado}")
        return resultado

    # ... (outros métodos para multiplicação, divisão, etc.)

    def mostrar_historico(self):
        print("Histórico de operações:")
        for operacao in self.historico:
            print(operacao)

# Exemplo de uso:
calculadora = Calculadora()
resultado1 = calculadora.somar(5, 3)
resultado2 = calculadora.subtrair(10, 4)
calculadora.mostrar_historico()


# 27 Crie uma classe Animal com um método mover que imprima uma mensagem indicando como ele se move (exemplo: "O peixe nada").
class Animal:
    def mover(self):
        print("O animal se move.")

class Peixe(Animal):
    def mover(self):
        print("O peixe nada.")

class Cachorro(Animal):
    def mover(self):
        print("O cachorro corre.")

# Exemplo de uso:
peixe1 = Peixe()
cachorro1 = Cachorro()

peixe1.mover()  # Saída: O peixe nada.
cachorro1.mover()  # Saída: O cachorro corre.


# 28 Crie uma classe Banco que contenha várias ContaBancaria. Adicione um método para listar os saldos de todas as contas.
class ContaBancaria:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_saldos(self):
        for conta in self.contas:
            print(f"Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}")

# Exemplo de uso:
banco = Banco()

conta1 = ContaBancaria("João Silva", 12345, 1000)
conta2 = ContaBancaria("Maria Santos", 67890, 500)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

banco.listar_saldos()


# 29 Crie uma classe Jogo com atributos nome e pontuacao. Adicione métodos para iniciar o jogo e registrar a pontuação
class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciar_jogo(self):
        print(f"Iniciando o jogo {self.nome}!")

    def registrar_pontuacao(self, nova_pontuacao):
        self.pontuacao = nova_pontuacao
        print(f"Nova pontuação registrada: {self.pontuacao}")

# Exemplo de uso:
jogo1 = Jogo("Adivinhação")
jogo1.iniciar_jogo()
jogo1.registrar_pontuacao(100)

# 30 Crie uma classe Carro com os atributos marca e combustivel. Adicione métodos para abastecer e verificar o nível de combustível.
class Carro:
    def __init__(self, marca, combustivel=0):
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, litros):
        self.combustivel += litros
        print(f"Abastecido {litros} litros. Tanque com {self.combustivel} litros.")

    def verificar_combustivel(self):
        print(f"Nível de combustível: {self.combustivel} litros.")

# Exemplo de uso:
meu_carro = Carro("Fiat", 30)
meu_carro.verificar_combustivel()
meu_carro.abastecer(20)
meu_carro.verificar_combustivel()


