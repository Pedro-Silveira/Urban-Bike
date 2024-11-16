from models.ContaUrbanBike import ContaUrbanBike

class PedalPop(ContaUrbanBike):
    def __init__(self, numeroConta, saldo, taxaOperacao):
            super().__init__(numeroConta, saldo)
            self.taxaOperacao = taxaOperacao

    def pedalar(self, valor):
        try:
            valor           = float(valor)
            totalOperacao   = valor + self.taxaOperacao

            if (totalOperacao <= self.saldo):
                self.saldo -= totalOperacao

                return f"\nPedalada executada com sucesso! Total da operação: {totalOperacao} (c/ taxa)."
            
            return '\nVocê não tem saldo suficiente para pedalar.'
        except:
            return '\nO valor informado é inválido!'

    def creditar(self, valor):
        try:
            valor = float(valor)

            if (valor > 0):
                self.saldo += valor

                return f"\nValor creditado com sucesso! Novo saldo: {self.saldo}."

            return '\nO valor do crédito precisa ser maior do que zero.'
        except:
            return '\nO valor informado é inválido!'

    def mostrarDados(self):
        print(
            '\nExibindo dados da conta: \n\n',
            f"Número da Conta: {self.numeroConta}, \n",
            'Tipo: PedalPop, \n',
            f"Saldo: {self.saldo}, \n",
            f"Taxa de Operação: {self.taxaOperacao}."
        )