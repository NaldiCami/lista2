n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

sn = n1 + n2

if sn >= 60 and n1>=40 and n2 >=40:
    print("Parabéns, você passou!")
else: 
    print("Reprovado.")