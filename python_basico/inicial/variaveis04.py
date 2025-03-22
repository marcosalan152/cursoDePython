
print("-"*42)
print("Bem vindos ao formulário de contato.")
print("-"*42)

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
print("-"*60)
print("Informe seu endereço conforme os campos abaixo.")
print("-"*60)
rua = str(input("Digite o nome da sua Rua: "))
numero = int(input("Digite o número: "))
complemento = str(input("COMPLEMENTO: (casa) ou (ap/número): "))

print(f"Meu nome é {nome}\nMinha idade é {idade} anos\nMeu endereço completo é {rua, numero, complemento}")