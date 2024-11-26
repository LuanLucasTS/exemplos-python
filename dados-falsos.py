import sqlite3
import pyodbc
from faker import Faker
from faker_vehicle import VehicleProvider

# sQlite3 / executa a primeira vez pra criar a tabela
'''
conn = sqlite3.connect('dados-teste/clientes.db')
cursor = conn.cursor()
'''

# SQL Server
dados_conexao = (
    "Driver={SQL Server};"
    "Server=GAIA\SQLEXPRESS01;"
    "Database=teste;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# SQL Server
cria_TBusuario = """
IF OBJECT_ID(N'dbo.usuario', N'U') IS NULL
create table usuario(
	id_usuario int not null identity primary key,
	nome varchar(50),
	sobrenome varchar(50),
	rua varchar(50),
	numero int,
	bairro varchar(50),
	cidade varchar(50),
	estado varchar(50),
	celular varchar(50),
	email varchar(50),
	usuario varchar(50),
	senha varchar(50),
	cpf varchar(50),
	rg varchar(50),
	nascimento varchar(20),
)
"""
# SQL Server
cria_TBveiculo = """
IF OBJECT_ID(N'dbo.veiculo', N'U') IS NULL
create table veiculo(
    id_veiculo int identity (1, 1) primary key,
    id_usuario int not null,
    CONSTRAINT FK_usuario FOREIGN KEY (id_usuario)
        REFERENCES usuario (id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    marca varchar(50),
    modelo varchar(50),
    ano int,
    placa varchar(20),
    
        
)
"""

cursor.execute(cria_TBusuario)
cursor.execute(cria_TBveiculo)

fake = Faker(locale='pt-br')
fake.add_provider(VehicleProvider)
fake.seed_instance(333)

for i in range(1000):
    #Usuario
    nome = fake.first_name()
    sobrenome = fake.last_name()
    rua = fake.street_name()
    numero = fake.building_number()
    bairro = fake.bairro()
    cidade = fake.city()
    estado = fake.estado_nome()
    celular = fake.cellphone_number()
    email = fake.email()
    usuario = fake.user_name()
    senha = fake.password()
    cpf = fake.cpf()
    rg = fake.rg()
    nascimento = fake.date_of_birth()
    nascimento = str(nascimento) #tive que converter datetime em string pois tava dando erro no sql server
    #Veiculo
    marca = fake.vehicle_make()
    modelo = fake.vehicle_model()
    ano = fake.vehicle_year()
    placa = fake.license_plate()

    sql = "INSERT INTO usuario (nome, sobrenome, rua, numero,  bairro, cidade, estado, celular, email, usuario, senha, cpf, rg, nascimento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, nome, sobrenome, rua, numero,  bairro, cidade, estado, celular, email, usuario, senha, cpf, rg, nascimento)
    cursor.execute(f"INSERT INTO veiculo (id_usuario, marca, modelo, ano, placa) VALUES ((SELECT MAX(id_usuario) FROM usuario), '{marca}', '{modelo}', {ano}, '{placa}')")

cursor.commit()
