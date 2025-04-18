
while True:
    menu=('''
        [1] - Cadastro de pessoas,
        [2] - Cadastro de lista de mercado,
        [3] - sair
    ''')
    opc = int(input("Escolha uma opção do menu: "))

    if opc == 1:
        print("Bem vindo ao cadastro de pessoas!")
        for pessoa in range(1,11):
            nome = str(input(f"Digite o {pessoa}º nome: "))

            while True:
                try:
                    idade = int(input("Digite a idade: "))
                except(ValueError, TypeError):
                    print("ERRO: Por favor digite uma idade válida.")
                    continue
                else:
                    break

            sexo = str(input("Digite o sexo [Mf]: ")).strip().strip().upper()[0]
            while sexo not in 'f/m':
                print("ERRO: Por favor digite [m ou f] para o sexo.")
                sexo = str(input("Digite o sexo [Mf]: ")).strip().strip().upper()[0]
                break

    elif opc == 2:
        print("Crie sua lista de mercado!")
        produtos = str(input("Digite os itens: "))

    elif opc == 3:
        print("\033[7;34;41mObrigado por usar nosso sistema! Até logo!\033[m")
        break
    else:
        print("ERRO: por favor escolha uma opção válida do menu.")