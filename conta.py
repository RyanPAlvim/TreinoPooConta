from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agência: int, número_da_conta: int, saldo: float = 0):
        self.agencia = agência
        self.numero_conta = número_da_conta
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.detalhes(f'Depósito de {valor} efetuado.')
        return

    @abstractmethod
    def sacar(self):
        pass

    def detalhes(self, msg: str = ''):
        print(msg)
        print(f'Seu saldo é: {self.saldo}.')

    def __repr__(self):
        attrs = ', '.join(f'{k.lstrip('_')}: {v!r}' for k,
                          v in self.__dict__.items())
        return f'{self.__class__.__name__}({attrs})'


class ContaCorrente(Conta):

    def __init__(self, agência: int,
                 número_da_conta: int,
                 saldo: float = 0,
                 limite_máximo: float = 0
                 ):
        super().__init__(agência, número_da_conta, saldo)
        self.limite = limite_máximo

    def sacar(self, valor: float) -> None:

        valor_pos_saque = self.saldo - valor

        if valor <= 0:
            raise ValueError('Não é possível sacar valores negativos ou 0')

        if valor_pos_saque < -self.limite:
            print(f'Impossível sacar esse valor. Máximo saque: '\
                  f'{self.limite + self.saldo}')
            return

        self.saldo -= valor
        self.detalhes(f'Saque realizado no valor de {valor}.')


class ContaPoupança(Conta):

    def sacar(self, valor: float) -> None:

        valor_pos_saque = self.saldo - valor

        if valor <= 0:
            raise ValueError('Não é possível sacar valores negativos ou 0')

        if valor_pos_saque < 0:
            print(f'Impossível sacar tal valor. Máximo para sacar: '\
                  f'{self.saldo}')
            return

        self.saldo -= valor
        self.detalhes(f'Saque ralizado no valor de {valor}.')

