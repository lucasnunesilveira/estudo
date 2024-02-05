from time import time, sleep
def velocidade (funcao):
    def interna (*args,**kwargs):
        star_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time-star_time)*1000
        print(f'A função  {funcao.__name__} levou { tempo :.2f}ms para executar')
    return interna

@velocidade
def demora():
    for i in range(5):
        sleep(1)

demora()

