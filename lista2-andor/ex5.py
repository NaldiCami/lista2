ler = input("Você sabe ler? (S/N): ")
if ler != "S":
    print("Não Ok")
else:
    escrever = input("Escreva a seguinte frase: 'Eu sou legal': ")
    if escrever != "Eu sou legal":
        print("Não Ok")
    else:
        idade = int(input("Qual é a sua idade? "))
        if idade < 25:
            print("Não OK")
        else:
            print("Tudo Ok!")