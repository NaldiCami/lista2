n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2+n3:
    print("{} é maior do que a soma de {} e {}".format(n1,n2,n3))
elif n2 > n1+n3:
    print("{} é maior do que a soma de {} e {}".format(n2,n1,n3))
elif n3 > n1+n2:
    print("{} é maior do que a soma de {} e {}".format(n3,n2,n1))
else:
    print("Nenhum número é maior do que a somas dos outros dois.")