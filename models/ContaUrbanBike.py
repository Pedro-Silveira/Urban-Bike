from abc import abstractmethod
from interfaces.Imprimivel import Imprimivel

class ContaUrbanBike(Imprimivel):
    def __init__(self, numeroConta, saldo = 0.0):
        self.numeroConta = numeroConta
        self.saldo = saldo

    @abstractmethod
    def pedalar(self):
        # Método para gastar os créditos.
        pass

    @abstractmethod
    def creditar(self):
        # Método para carregar créditos na carteira.
        pass

    def transferir(self, valor, contaDestino):
        try:
            valor = float(valor)

            if (self.saldo >= valor):
                self.pedalar(valor)
                contaDestino.creditar(valor)

                return 'Transferência realizada com sucesso.'

            return 'Você não tem saldo suficiente para executar essa transferência.'
        except:
            return 'O valor informado é inválido!'