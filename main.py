from conta import ContaCorrente, ContaPoupança
from banco import Banco
from cliente import Cliente

banco_atlas = Banco()

ryan = Cliente('Ryan', 18)
carlos = Cliente('Carlos', 18)

cc1 = ContaCorrente(111, 342, 2000, 5000)
cp1 = ContaPoupança(222, 284, 10000)
cp2 = ContaPoupança(333, 516, 3000)

ryan.conta = cc1
carlos.conta = cp1

banco_atlas.clientes.extend([ryan, carlos])
banco_atlas.contas.extend([cc1, cp1])
banco_atlas.agencias.extend([111, 222])

#Autenticação funcinando pois a conta realmente é do cliente e pertence ao banco.
if banco_atlas.autenticar(ryan, cc1):
    cc1.depositar(100)
    cc1.sacar(10)
    cc1.depositar(10)

#Autenticação falha e nada será executado, pois a conta não é desse cliente e nem pertence ao banco.
if banco_atlas.autenticar(carlos, cp2):
    cp2.sacar(200)
    