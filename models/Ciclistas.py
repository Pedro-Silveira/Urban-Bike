class Ciclistas():
    def __init__(self):
        self.listaPedais = []

    def inserir(self, pedal):
        if (isinstance(self.procurarPedal(pedal.numeroConta), str)):
            self.listaPedais.append(pedal)

            return '\nO pedal foi inserido com sucesso.'

        return '\nNão é possível inserir o pedal pois ele já está na lista.'

    def remover(self, idPedal):
        conta = self.procurarPedal(idPedal)

        if (not isinstance(conta, str)):
            self.listaPedais.remove(conta)

            return '\nO pedal foi removido com sucesso. \n'

        return '\nNão é possível remover o pedal pois ele não está na lista. \n'

    def procurarPedal(self, idPedal):
        try:
            idPedal = int(idPedal)
            pedal   = next((obj for obj in self.listaPedais if obj.numeroConta == idPedal), None)

            return pedal or '\nNão foi encontrado um pedal com o número da conta informado. \n'
        except:
            return '\nO número da conta informado é inválido.'

    def listarPedais(self):
        if (len(self.listaPedais) > 0):
            for pedal in self.listaPedais:
                pedal.mostrarDados()

            print('\n')
        else:
            print('\nNão existem pedais disponíveis para listar. \n')