from abc import abstractmethod
from interfaces.Imprimivel import Imprimivel

class ContaUrbanBike(Imprimivel):
    def __init__(self, numeroConta, saldo = 0.0):
        self.numeroConta    = numeroConta
        self.saldo          = saldo

    @abstractmethod
    def pedalar(self):
        # Método para gastar os créditos.
        pass

    @abstractmethod
    def creditar(self):
        # Método para carregar créditos na carteira.
        pass

    def transferir(self, valor, contaOrigem, contaDestino):
        try:
            valor           = float(valor)
            taxaOperacao    = float(getattr(contaOrigem, 'taxaOperacao', 0))

            # Impede o usuário de realizar transferências com valores menores ou iguais a 0.
            if (valor < 0):
                return '\nO valor da transferência precisa ser maior do que zero.'

            # Impede o usuário sem saldo suficiente de realizar transferências
            if (contaOrigem.saldo < valor + taxaOperacao):
                return '\nVocê não tem saldo suficiente para realizar esta transferência.'

            contaOrigem.pedalar(valor)
            contaDestino.creditar(valor)

            return '\nTransferência realizada com sucesso.'
        except:
            return '\nO valor informado é inválido!'