from interfaces import Imprimivel

class Ciclistas(Imprimivel):
    def __init__(self, listaPedais: list):
        self.listaPedais = listaPedais

    def iserir(self, pedal):
        if (not self.listaPedais.__contains__(pedal)):
            self.listaPedais.append(pedal)

            return 'O pedal foi inserido com sucesso.'

        return 'Não é possível inserir o pedal pois ele já está na lista.'

    def remover(self, pedal):
        if (self.listaPedais.__contains__(pedal)):
            self.listaPedais.remove(pedal)

            return 'O pedal foi removido com sucesso.'

        return 'Não é possível remover o pedal pois ele não está na lista.'

    def procurarPedal(self, idPedal):
        if (self.listaPedais[idPedal]):
            return self.listaPedais[idPedal]

        return 'Não foi encontrado um pedal com o ID informado.'

    def listarPedais(self):
        for pedal in self.listaPedais:
            pedal.mostrarDados