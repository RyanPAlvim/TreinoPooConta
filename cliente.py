from abc import ABC
import conta


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        nome_confirmado = list(nome)
        for letra in nome_confirmado[:]:
            if letra in '1234567890':
                nome_confirmado.remove(letra)
        nome_final = ''
        self._nome = nome_final.join(nome_confirmado)

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        attrs = ', '.join(f'{k.lstrip('_')}: {v!r}' for k,v in self.__dict__.items())
        return f'{self.__class__.__name__}({attrs})'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None
