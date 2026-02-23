from datetime import datetime


class Transacoes:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []

    def entradas(self, valor, categoria):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append({"categoria": categoria, "valor": valor})

    def saidas(self, valor, categoria):
        if valor > 0:
            self.saldo -= valor
            self.transacoes.append({"categoria": categoria, "valor": valor})
            

    def extrato(self):
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("\nTransações:")
        for e in self.transacoes:
            print(f"{e['categoria']}: R$ {abs(e['valor']):.2f}")



    


    
    


      
    
    

    