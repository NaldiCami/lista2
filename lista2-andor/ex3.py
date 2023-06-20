idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade, pode entrar.")
else:
    perm = input("Você tem permissão dos seus pais? (S/N) ")
    if perm == "S":
        print("Você pode entrar.")
    else:
        print("Você não pode entrar!")