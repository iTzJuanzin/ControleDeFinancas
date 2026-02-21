from transacoes import Transacoes

transacoes = Transacoes()

while True:
        print("\n" + "=" * 40)
        print("  💰 CONTROLE FINANCEIRO PESSOAL")
        print("=" * 40)
        print("[1] Adicionar entrada (receita)")
        print("[2] Adicionar saída (despesa)")
        print("[3] Ver extrato")
        print("[4] Sair")
        print("=" * 40)


        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
           valor = float(input("Quantos R$ entrou ? "))
           categoria = input("Qual a categoria que deseja definir ? ")
           transacoes.entradas(valor, categoria)
           print("✅ Entrada registrada!")

        elif opcao == "2":
            valor = float(input("Quantos R$ saiu ? "))
            categoria = input("Qual a categoria que deseja definir ? ")
            transacoes.saidas(valor, categoria)
            print("✅ Saída registrada!")

        elif opcao == "3":
            transacoes.extrato()
            
        elif opcao == "4":
            print("Até logo! 👋")
            break

        else:
            print("❌ Opção inválida!")



