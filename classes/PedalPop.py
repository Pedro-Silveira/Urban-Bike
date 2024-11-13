from models.ContaUrbanBike import ContaUrbanBike

class PedalPop(ContaUrbanBike):
    def __init__(self, numeroConta, saldo, taxaOperacao):
        try:
            numeroConta = int(numeroConta)
            saldo = float(saldo)
            taxaOperacao = float(taxaOperacao)

            super().__init__(numeroConta, saldo)
            self.taxaOperacao = taxaOperacao
        except:
            return 'Os valores informados para o cadastro da conta são inválidos.'

    def pedalar(self, valor):
        try:
            valor = float(valor)
            totalOperacao = valor + self.taxaOperacao

            if (totalOperacao <= self.saldo):
                self.saldo -= totalOperacao

                return "Pedalada executada com sucesso! Novo saldo: {self.saldo}."
            
            return 'Você não tem saldo suficiente para pedalar.'
        except:
            return 'O valor informado é inválido!'

    def creditar(self, valor):
        try:
            valor = float(valor)

            if (valor > 0):
                self.saldo += valor

                return "Valor creditado com sucesso! Novo saldo: {self.saldo}."

            return 'O valor do crédito precisa ser maior do que zero.'
        except:
            return 'O valor informado é inválido!'

    def mostrarDados(self):
        print(
            'Exibindo dados da conta: \n\n',
            "Número da Conta: {self.numeroConta}, \n",
            'Tipo: PedalPop, \n',
            "Saldo: {self.saldo}, \n",
            "Taxa de Operação: {self.taxaOperacao}."
        )