#comentário de uma linha
"""comentário de várias
linhas"""

#comando print - mostra a saida do dado
print("Exemplo 1")
print("Exemplo 2 de Pular \nLinha")

x = 20
print("Eu tenho" ,x, "anos")

y=10
z=20
w=30

print("Tenho 3 variáveis:",y,z,w)
print("Y (10) + Z (20) + W (30) =",y+z+w)

soma = y + z + w
print("Soma = ",soma)


div = w/y
print("Divisão de W (",w,")por Y(",y,") = ",div)

div_int= w//y
print("Divisao dos valores W e Y com resultado INTEIRO:",div_int)

elevado = y ** 2
print("A potencia de y (10) é:",elevado)


sub = w-y

print("O valor da subtração é:", sub)

print("O valor da subtração de {}-{}= {}".format(w,y,w-y))


#operadores relacionais

d=2
e=5

print(d==e)
print(d>e)
print(d<e)
print(d>=e)
print(d<=e)


m = input("Qual teu nome?")
print(m)

n1=int(input("Digite o primeiro numero:"))
n2=int(input("Digite o segundo numero:"))
print("A soma de {} + {} = {}".format(n1,n2,n1+n2))


num2 = 2
num3 = 3
num4 = 4
num5 = 5
num10= 10
num12= 12

print("{}-{} = {} + {} = {} * {} = {} - {} = {} + {} = {}".format(num12,num10,num12-num10,num2,num12-num10+num2,num4,(num12-num10+num2)*num4,num3,(num12-num10+num2)*num4-num3,num5,(num12-num10+num2)*num4-num3+num5))
"""Lista 1 de Exercícios

1. Orgnaize os números 2,3,4,5,10,12 para obter a saida 18 em uma única operação
"""
