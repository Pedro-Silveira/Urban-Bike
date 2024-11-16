from models.Ciclistas import Ciclistas
from classes.PedalPop import PedalPop
from classes.PedalPremium import PedalPremium

class Main():
    def __init__(self):
        self.ciclistas = Ciclistas()

    def executar(self):
        escolha = '0'

        while (escolha != '5'):
            print(
                'Bem-vindo ao Urban Bike! \n\n',
                'Por gentileza, selecione uma das opções abaixo: \n',
                '1 - Criar pedal; \n',
                '2 - Remover pedal; \n',
                '3 - Gerar relatório; \n',
                '4 - Selecionar um pedal; ou \n',
                '5 - Finalizar. \n'
            )

            escolha = input().strip()

            match escolha:
                case '1':
                    self.criarPedal()
                case '2':
                    print(self.removerPedal())
                case '3':
                    self.gerarRelatorio
                case '4':
                    idPedal = input('\nInforme o número da conta do pedal a ser selecionado: \n').strip()
                    pedal = self.ciclistas.procurarPedal(idPedal)

                    if isinstance(pedal, PedalPop) or isinstance(pedal, PedalPremium):
                        self.selecionarPedal(pedal)

                    print(pedal)
                case '5':
                    print('\nObrigado por utilizar nosso sistema, até breve! \n')
                case _:
                    print('\nPor gentileza, informe uma opção válida! \n')

    def criarPedal(self):
        tipoPedal = '0'

        while tipoPedal != '3':
            print(
                '\nEscolha o tipo do pedal abaixo: \n\n',
                '1 - PedalPop; \n',
                '2 - PedalPremium; ou \n',
                '3 - Cancelar. \n'
            )

            tipoPedal = input().strip()

            match tipoPedal:
                case '1':
                    numeroConta = input('\nInforme o número da conta: \n')
                    saldo = input('\nInforme o saldo da conta: \n')
                    taxaOperacao = input('\nInforme a taxa de operação da conta: \n')

                    pedal = PedalPop(numeroConta, saldo, taxaOperacao)

                    if (isinstance(pedal, PedalPop)):
                        print(self.ciclistas.inserir(pedal))

                    print(pedal)
                case '2':
                    numeroConta = input('\nInforme o número da conta: \n')
                    saldo = input('\nInforme o saldo da conta: \n')
                    limite = input('\nInforme o limite da conta: \n')

                    pedal = PedalPremium(numeroConta, saldo, limite)

                    if (isinstance(pedal, PedalPremium)):
                        print(self.ciclistas.inserir(pedal))

                    print(pedal)
                case '3':
                    print('\nOperação cancelada... \n')
                case _:
                    print('\nPor gentileza, informe uma opção válida!')

    def removerPedal(self):
        idPedal = input('Informe o ID do pedal a ser excluído: \n').strip()

        return self.ciclistas.remover(idPedal)

    def gerarRelatorio(self):
        self.ciclistas.listarPedais()

    def selecionarPedal(self, pedal):
        opcaoPedal = '0'

        while opcaoPedal != '5':
            print(
                f"\nEscolha qual ação deseja executar com o pedal {pedal.numeroConta}: \n\n",
                '1 - Creditar; \n',
                '2 - Pedalar; \n',
                '3 - Transferir; \n',
                '4 - Gerar relatório; ou \n',
                '5 - Cancelar. \n'
            )

            opcaoPedal = input().strip()

            match opcaoPedal:
                case '1':
                    valor = input('\nInforme o valor a ser creditado: \n')

                    print(pedal.creditar(valor))
                case '2':
                    valor = input('\nInforme o valor a ser pedalado: \n')

                    print(pedal.pedalar(valor))
                case '3':
                    valor   = input('\nInforme o valor a ser transferio: \n')
                    idPedal = input('\nInforme o ID da conta do remetente: \n')

                    contaDestino = self.ciclistas.procurarPedal(idPedal)

                    if isinstance(contaDestino, PedalPremium) or isinstance(contaDestino, PedalPop):
                        print(pedal.transferir(valor, contaDestino))

                    print(pedal)
                case '4':
                    pedal.mostrarDados()
                case _:
                    print('\nPor gentileza, informe uma opção válida! \n')

if (__name__ == '__main__'):
    app = Main()
    app.executar()