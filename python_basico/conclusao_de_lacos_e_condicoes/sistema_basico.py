from  time import sleep

while True:
    menu = ('''
    [1] = Cadastro pessoal,
    [2] - Lista de compras,
    [3] - sair
    ''')
    print(menu)
    opc = int(input("Escolha uma opção do menu: "))

    if opc == 1:
        print("Bem vindos ao sistema de cadastro de pessoas")
        for pessoas in range(1, 2):
            nome = str(input(f"Digite o nome da {pessoas}ª pessoa: "))

            while True:
                try:
                    idade = int(input("Digite a idade: "))
                except(ValueError, TypeError):
                    print("ERRO: Por favor digite um valor de idade válido.")
                    continue
                else:
                    break

            sexo = str(input("Digite o sexo [m/f]: ")).strip().upper()[0]
            while sexo not in 'MmFf':
                print("ERRO: Por favor digite um sexo válido.")
                sexo = str(input("Digite o sexo [m/f]: ")).strip().upper()[0]

    elif opc == 2:
        print("Digite seus itens de compra")
        itens = str(input("Digite seus itens para compras: "))

    elif opc == 3:
        print("Obrigado por usar nosso sistema! Até logo!")
        break
    else:
        print("ERRO: Por favor escolha uma opção válida do menu.")


    sleep(2)
print(nome, idade, sexo)

