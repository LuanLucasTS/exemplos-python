a = 'concatenando'
b = 'string'

#usando modulo %
concatenamento = ("%s %s" % (a,b))
print(concatenamento)

#usando format
concatenamento = ('{} {}'.format(a, b))
print(concatenamento)


#usando string literal
concatenamento = f'{a} {b}'
print(concatenamento)