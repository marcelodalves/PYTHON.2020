#operadores de comparação >, <, >=, <=, !=, ==

a=2
b=4

print("A é maior que B: ",a>b)
print("B e maior que A: ",b>a)
print("A é igual a B: ", a==b)
print("A é diferente de B: ",a!=b)
print("A é maior e igual a B: ",a>=b)
print("A é menor e igual a B: ",a<=b)

x=int(input("Entre com um numero X: "))
y=int(input("Entre com um numero Y: "))

print("X eh maior q Y: ", x>y)
print("Y eh maior q X: ",y>x)

n1=input("Digite um valor string")
n2=int(input("Entre com um numero: "))
print(type(n1))
print(type(n2))

import math #importa todas as funcionalidades matematicas
num=int(input("Digite um numero"))
raiz = math.sqrt(num)
print("A raiz quadrada de {} é igual a {}".format(num,math.ceil(raiz))) #ceil arredonda pra cima

#outra maneira d fazer o import, usando o from

from math import sqrt, floor

num = int(input("Digite um number:"))
raiz = math.sqrt(num)
print("A raiz quadrada de {} [e igual a {}".format(num,math.floor(raiz))) #floor arredonda pra baixo

#para gerar numeros aleatorios entre 0 e 1

import random

num1=random.random()
print(num1)


import random
num2=random.randint(1,60)
print(num2)

import random
print(random.randrange(1,20))

# Fatiamento de cadeia de caracteres(textos) - strngs


frase=("Aprendendo Python com 4G!!!!!!!!!!!!!!!")
print(frase)
print(frase[4])
print(frase[11:18])
print(frase[11:22:2])
print(frase[:18])

# len () para saber o tamanho de uma string
print("A quantidade de caracteres na frase eh: ",len(frase))

# count() - para contar a quantidade de vezes q uma determinada letra se repete

print("A letra n se repete ",frase.count('n'))

# find () - para saber a posiçao de uma deterinada string
print(frase.find("Python"))

# in() para saber se uma determinada string existe
print("Python" in frase)

# replace() para alterar a palavra na frase, sem alterar a mesma
print(frase.replace("Python","PHP"))
