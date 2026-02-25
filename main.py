import pandas as pd
from openpyxl.styles import numbers
from transacoes import Transacoes


transacoes = Transacoes()

while True:
        print("\n" + "=" * 40)
        print("  💰 CONTROLE FINANCEIRO PESSOAL")
        print("=" * 40)
        print("[1] Adicionar entrada (receita)")
        print("[2] Adicionar saída (despesa)")
        print("[3] Ver extrato")
        print("[4]  Exportar extrato para Excel")
        print("[5] Sair")
        print("=" * 40)


        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
           valor = float(input("Quantos R$ entrou ? "))
           descricao = input("Qual a descrição da entrada ? ")
           transacoes.entradas(valor, descricao)
           print("✅ Entrada registrada!")

        elif opcao == "2":
            valor = float(input("Quantos R$ saiu ? "))
            descricao = input("Qual a descrição da saída ? ")
            transacoes.saidas(valor, descricao)
            print("✅ Saída registrada!")

        elif opcao == "3":
            transacoes.extrato()

        elif opcao == "4":
             df = pd.DataFrame(transacoes.transacoes)
             df["Saldo"] = transacoes.saldo
             df.to_excel("ExtratoMensal.xlsx", sheet_name="Extrato", index=False)

             
             print("✅ Extrato exportado para 'ExtratoMensal.xlsx'!")

              
             
             
             
            
        elif opcao == "5":
            print("Até logo! 👋")
            break

        else:
            print("❌ Opção inválida!")



