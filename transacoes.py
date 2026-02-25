import pandas as pd
from datetime import datetime


class Transacoes:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []

    def entradas(self, valor, descricao, tipo="+ entrada"):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append({"tipo": tipo, "Descrição": descricao, "valor": valor})
        else:
            print("Valor invalido, por favor insira um valor valido.")


    def saidas(self, valor, descricao, tipo="- saida"):
        if valor > 0:
            self.saldo -= valor
            self.transacoes.append({"tipo": tipo, "Descrição": descricao, "valor": valor})
        else:
            print("Valor invalido, por favor insira um valor valido.")

    def extrato(self):
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("\nTransações:")
        if self.transacoes == []:
            print("Nenhuma transação registrada.")
        else:
            for e in self.transacoes:
                print(f"{e['tipo'].upper()} - {e['Descrição']}: R$ {abs(e['valor']):.2f}")



    


    
    


      
    
    

    