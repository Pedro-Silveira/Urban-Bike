from abc import ABC, abstractmethod

class ContaUrbanBike(ABC):
    def __init__(self, numeroConta, saldo = 0.0):
        self.numeroConta = numeroConta,
        self.saldo = saldo

    @abstractmethod
    def pedalar(self):
        # Método para gastar os créditos.
        pass

    @abstractmethod
    def creditar(self):
        # Método para carregar créditos na carteira.
        pass