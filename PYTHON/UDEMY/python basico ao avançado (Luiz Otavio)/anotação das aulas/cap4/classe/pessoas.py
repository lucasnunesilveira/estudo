from datetime import datetime


class Pessoas:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))  # atributo da classe ela é visivel pela classe toda

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode fala comendo')
            return
        if self.falando:
            print(f'{self.nome}  ja estar falando')
            return
        print(f'{self.nome} estar falando sobre {assunto}')
        self.falando = True

    def para_falar(self):
        if not self.falando:
            print(f'{self.nome} não estar falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} already be eating.')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} be eating {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} not be eating')
            return
        print(f'{self.nome} stopped eating')
        self.comendo = False

    def get_dade(self):
        return self.ano_atual - self.idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# def instancia(atributos)
