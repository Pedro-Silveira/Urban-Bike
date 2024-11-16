class Ciclistas():
    def __init__(self):
        self.listaPedais = []

    def inserir(self, pedal):
        if (not self.listaPedais.__contains__(pedal)):
            self.listaPedais.append(pedal)

            return '\nO pedal foi inserido com sucesso.'

        return 'Não é possível inserir o pedal pois ele já está na lista.'

    def remover(self, pedal):
        if (self.listaPedais.__contains__(pedal)):
            self.listaPedais.remove(pedal)

            return 'O pedal foi removido com sucesso.'

        return 'Não é possível remover o pedal pois ele não está na lista.'

    def procurarPedal(self, idPedal):
            idPedal = int(idPedal)
            pedal   = next((obj for obj in self.listaPedais if obj.numeroConta == idPedal), None)

            return pedal or '\nNão foi encontrado um pedal com o número da conta informado. \n'

    def listarPedais(self):
        for pedal in self.listaPedais:
            pedal.mostrarDados