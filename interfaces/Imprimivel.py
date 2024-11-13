from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def mostrarDados(self):
        # Interface para mostrar os atributos.
        pass