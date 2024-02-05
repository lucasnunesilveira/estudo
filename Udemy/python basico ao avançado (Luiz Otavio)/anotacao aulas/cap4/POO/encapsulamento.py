"""
public => a classe fica visivel para todos
protected => fica visivel para sua subclass
private => fica visivel somente na classe
_ privado ( maneira mais fraca)  protected
__privado ( maneira mais FORTE ) private
"""


class BaseDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(f"ID é {id} e o nome é {nome} ")

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDados()
print(bd._dados)

