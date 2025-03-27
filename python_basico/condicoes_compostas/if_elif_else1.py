
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("menor de idade.")
elif idade <21:
    print("Você ainda não é maior de idade ")
elif idade < 65:
    print("Você é maior de idade.")
elif idade < 100:
    print("Você está na melhor idade.")
else:
    print("Por favor digite um valor inteiro válido.")

