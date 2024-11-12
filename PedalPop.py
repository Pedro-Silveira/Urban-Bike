from models.ContaUrbanBike import ContaUrbanBike

class PedalPop(ContaUrbanBike):
    def __init__(self, numeroConta, saldo, taxaDeOperacao):
        super().__init__(numeroConta, saldo)
        self.taxaDeOperacao = taxaDeOperacao

    def pedalar(self, valor):
        totalOperacao = valor + self.taxaDeOperacao

        if (totalOperacao <= self.saldo):
            self.saldo -= totalOperacao

            return "Pelada executada com sucesso! Novo saldo: {self.saldo}."
        
        return "Você não tem saldo suficiente para pedalar."

    def creditar(self, valor):
        if (valor > 0) {
            self.saldo += valor

            return "Valor creditado com sucesso! Novo saldo: {self.saldo}."
        }

        return "O valor do crédito precisa ser maior do que zero."