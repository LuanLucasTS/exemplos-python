### Lista apenas com itens pares
# lista original
lista_completa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension para gerar lista de pares
lista_pares = [x for x in lista_completa if x % 2 ==0]

print(lista_completa)
print(lista_pares)

###Lista apenas com itens que terminem com A
#Lista original
nomes = ['joao', 'felipe', 'marcos', 'carla', 'ana']

# List Comprehension para gerar lista com nomes terminados em a
nomes_final_a = [x for x in nomes if x[-1] == 'a']
print(nomes)
print(nomes_final_a)
