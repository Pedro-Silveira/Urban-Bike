from models import Ciclistas
from classes import PedalPop, PedalPremium

class Main():
    def __init__(self):
        self.ciclistas = Ciclistas

    def executar(self):
        escolha = '0'
        while (escolha != '5'):
            print(
                'Bem-vindo ao Urban Bike! \n\n',
                'Por gentileza, selecione uma das opções abaixo \n',
                '1 - Criar pedal; \n',
                '2 - Remover pedal; \n',
                '3 - Gerar relatório; \n',
                '4 - Selecionar um pedal; ou \n',
                '5 - Finalizar. \n/\n'
            )

            escolha = input().strip()

            match escolha:
                case '1':
                    print(self.criarPedal)
                case '2':
                    print(self.removerPedal)
                case '3':
                    self.gerarRelatorio
                case '4':
                    idPedal = input('Informe o ID do pedal a ser selecionado: \n').strip()
                    pedal = self.ciclistas.procurarPedal(idPedal)

                    if isinstance(pedal, PedalPop) or isinstance(pedal, PedalPremium):
                        self.selecionarPedal(pedal)

                    return pedal
                case '5':
                    print('Obrigado por utilizar nosso sistema, até breve!')
                case _:
                    print('Por gentileza, informe uma opção válida!')

    def criarPedal(self):
        tipoPedal = '0'

        while tipoPedal != '3':
            print(
                'Escolha o tipo do pedal abaixo: \n\n',
                '1 - PedalPop; \n',
                '2 - PedalPremium; ou \n',
                '3 - Cancelar. \n\n'
            )

            tipoPedal = input().strip()

            match tipoPedal:
                case '1':
                    numeroConta = input('Informe o número da conta: \n')
                    saldo = input('\nInforme o saldo da conta: \n')
                    taxaOperacao = input('\nInforme a taxa de operação da conta: \n')

                    pedal = PedalPop(numeroConta, saldo, taxaOperacao)

                    if (isinstance(pedal, PedalPop)):
                        return self.ciclistas.inserir(pedal)

                    return pedal
                case '2':
                    numeroConta = input('Informe o número da conta: \n')
                    saldo = input('\nInforme o saldo da conta: \n')
                    limite = input('\nInforme o limite da conta: \n')

                    pedal = PedalPremium(numeroConta, saldo, limite)

                    if (isinstance(pedal, PedalPremium)):
                        return self.ciclistas.inserir(pedal)

                    return pedal
                case '3':
                    return '\nOperação cancelada... \n\n'
                case _:
                    return '\nPor gentileza, informe uma opção válida! \n\n'

    def removerPedal(self):
        idPedal = input('Informe o ID do pedal a ser excluído: \n').strip()

        return self.ciclistas.remover(idPedal)

    def gerarRelatorio(self):
        self.ciclistas.listarPedais()

    def selecionarPedal(self, pedal):
        opcaoPedal = '0'

        while opcaoPedal != '5':
            print(
                'Escolha qual ação deseja executar com o pedal: \n\n',
                '1 - Creditar; \n',
                '2 - Pedalar; \n',
                '3 - Transferir; \n',
                '4 - Gerar relatório; ou \n',
                '5 - Cancelar. \n\n'
            )

            opcaoPedal = input().strip()

            match opcaoPedal:
                case '1':
                    valor = input('Informe o valor a ser creditado: \n')

                    print(pedal.creditar(valor))
                case '2':
                    valor = input('Informe o valor a ser pedalado: \n')

                    print(pedal.pedalar(valor))
                case '3':
                    valor = input('Informe o valor a ser transferio: \n')
                    idPedal = input('\nInforme o ID da conta do remetente: \n')

                    contaDestino = self.ciclistas.procurarPedal(idPedal)

                    if isinstance(contaDestino, PedalPremium) or isinstance(contaDestino, PedalPop):
                        print(pedal.transferir(valor, contaDestino))

                    print(pedal)
                case '4':
                    pedal.mostrarDados()
                case _:
                    print('\nPor gentileza, informe uma opção válida! \n\n')

if (__name__ == '__main__'):
    Main.executar()