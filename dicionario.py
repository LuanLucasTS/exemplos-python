#Criando dicionário
#Forma1
a = dict(marca='Fiat', modelo='Marea', ano=1999)
print(a)

#Forma2
b = {'marca':'fiat', 'modelo': 'marea', 'ano': 1999}
print(b)

#clear. limpa todos os itens do dicionario
my_dict = {'name': 'Aisif', 'age': 25}
my_dict.clear()
print(my_dict)

#copy copia o dicionario sem alterar o original
my_dict = {'name': 'Aisif', 'age': 25}
new_dict = my_dict.copy()
new_dict['age'] = 30
print(my_dict)
print(new_dict)

#get. retorna o valor especifico de uma chave
my_dict = {'name': 'Aisif', 'age': 25}
age = my_dict.get('age')
print(age)
#tentando imprimir uma chave que nao existe
occupation = my_dict.get('occupation')
print(occupation)
#setando um valor padrao caso a chave nao exista
occupation = my_dict.get('occupation', 'desempregado')
print(occupation)

#itens. Retorna a lista de chaves e valores
my_dict = {'name': 'Aisif', 'age': 25}
itens = my_dict.items()
print(itens)

#keys. retorna a lista de chaves
my_dict = {'name': 'Aisif', 'age': 25}
keys = my_dict.keys()
print(keys)

#values. retorna a lista de valores
my_dict = {'name': 'Aisif', 'age': 25}
values = my_dict.values()
print(values)

#pop. remove e retorna um valor de chave
my_dict = {'name': 'Aisif', 'age': 25}
age = my_dict.pop ('age')
print(age)
print(my_dict)

#update. atualiza um valor
my_dict = {'name': 'Aisif', 'age': 25}
my_dict.update({'age': 30})
print(my_dict)
