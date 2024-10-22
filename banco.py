import conta, cliente

class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[cliente.Cliente] | None = None,
            contas: list[conta.Conta] | None = None):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def __repr__(self):
        attrs = ', '.join(f'{k}: {v!r}' for k,v in self.__dict__)
        return f'{self.__class__.__name__}({attrs})'

    def _confirma_agencia(self, conta:conta.Conta ):
        if conta.agencia in self.agencias:
            return True
        return False

    def _confirma_cliente(self, cliente:cliente.Cliente):
        if cliente in self.clientes:
            return True
        return False

    def _confirma_conta(self, conta:conta.Conta):
        if conta in self.contas:
            return True
        return False

    def _confirma_se_conta_e_de_cliente(self, conta: conta.Conta, cliente: cliente.Cliente):
        if cliente.conta is conta:
            return True
        return False
    
    def autenticar(self, cliente:cliente.Cliente, conta:conta.Conta):
        confirma = self._confirma_agencia(conta) and \
            self._confirma_cliente(cliente) and \
            self._confirma_conta(conta) and \
            self._confirma_se_conta_e_de_cliente(conta, cliente)
        
        if confirma == False:
            print('Confirmação mal sucedida...')
            return False
        return True
    

