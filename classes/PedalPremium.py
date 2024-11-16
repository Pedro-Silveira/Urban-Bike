from models.ContaUrbanBike import ContaUrbanBike

class PedalPremium(ContaUrbanBike):
    def __init__(self, numeroConta, saldo, limite):
        try:
            numeroConta = int(numeroConta)
            saldo = float(saldo)
            limite = float(limite)

            if (saldo < 100):
                return 'Para ser PedalPremium, você precisa creditar um mínimo de R$ 100,00 na carteira ao criar sua conta.'

            super().__init__(numeroConta, saldo)
            self.limite = limite
        except:
            return 'Os valores informados para o cadastro da conta são inválidos.'

    def pedalar(self, valor):
        try:
            valor = float(valor)

            if (self.saldo - valor >= -(self.limite)):
                self.saldo -= valor

                return f"Pedalada executada com sucesso! Novo saldo: {self.saldo}."

            return 'Você não tem saldo suficiente ou limite disponível para pedalar.'
        except:
            return 'O valor informado é inválido!'

    def creditar(self, valor):
        try:
            valor = float(valor)

            if (valor > 0):
                self.saldo += valor

                return f"Valor creditado com sucesso! Novo saldo: {self.saldo}."

            return 'O valor do crédito precisa ser maior do que zero.'
        except:
            return 'O valor informado é inválido!'

    def mostrarDados(self):
        print(
            '\nExibindo dados da conta: \n\n',
            f"Número da Conta: {self.numeroConta}, \n",
            'Tipo: PedalPremium, \n',
            f"Saldo: {self.saldo}, \n",
            f"Limite: {self.limite}."
        )