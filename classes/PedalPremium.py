from models.ContaUrbanBike import ContaUrbanBike

class PedalPremium(ContaUrbanBike):
    def __init__(self, numeroConta, saldo, limite):
        super().__init__(numeroConta, saldo)
        self.limite = limite

    def pedalar(self, valor):
        try:
            valor = float(valor)

            if (self.saldo - valor >= -(self.limite)):
                self.saldo -= valor

                return f"\nPedalada executada com sucesso! Novo saldo: {self.saldo}."

            return '\nVocê não tem saldo suficiente ou limite disponível para pedalar.'
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
            'Tipo: PedalPremium, \n',
            f"Saldo: {self.saldo}, \n",
            f"Limite: {self.limite}."
        )