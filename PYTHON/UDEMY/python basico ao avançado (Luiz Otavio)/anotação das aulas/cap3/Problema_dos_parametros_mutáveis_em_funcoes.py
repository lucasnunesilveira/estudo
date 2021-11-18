
def lista_total_de_clientes (clientes_iteravel,lista = None):
    if  lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista
cliente1 = lista_total_de_clientes(['joao','maria','lucas'])
cliente2 = lista_total_de_clientes(['renata','gabriella', 'isabella'])

print(cliente1)
print(cliente2)