'''1. Crie um  python que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor'''

inteiro = int(input("Entre com um numero I-N-T-E-I-R-O: "))
sucessor = inteiro+1
antecessor = inteiro-1
print("No valor {}, o seu sucessor é: {} e seu antecessor e: {}".format(inteiro,sucessor,antecessor))


'''2. Crie um  python que leia um numero e mostre o seu dobro, triplo e raiz quadrada.'''
import math

inteiro2 = int(input("Entre com outro numero I N T E I R O: "))
raiz = math.sqrt(inteiro2)
dobro = inteiro2*inteiro2
triplo = inteiro2*3

print("No valor {}, o seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}".format(inteiro2,dobro,triplo,math.ceil(raiz)))

'''3.Crie um  python que leia um valor em metros e a exiba convertido em centimetros e milimetros'''

metros = float(input("Entre com a medida em METROS: "))

centimetro = metros*100
milimetro = metros*1000

print("{} metros são {} centímetros, e também são {} milímetros".format(metros,centimetro,milimetro))

'''4. Crie um  python que leia um numero inteiro qualquer e mostre na tela a sua tabuada'''

tabuada = int(input("Entre com um valor para ser mostrada a TABUADA: "))

print("{}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {} -- {}x{} = {}".format(tabuada,1,tabuada*1,tabuada,2,tabuada*2,tabuada,3,tabuada*3,tabuada,4,tabuada*4,tabuada,5,tabuada*5,tabuada,6,tabuada*6,tabuada,7,tabuada*7,tabuada,8,tabuada*8,tabuada,9,tabuada*9,tabuada,10,tabuada*10))
       
'''5.Crie um  python que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere a US$1,00=R$4.20'''

dinheiro = float(input("Entre com a quantidade de DINHEIRO: "))
dolar = dinheiro/4.20
print("Você tem R${} e pode comprar {} dólares".format(dinheiro,dolar))

'''6.Crie um  python que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessária para pinta-la. Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados'''

larg = float(input("Entre com a largura da parede: "))
alt = float(input("Entre com a altura da parede: "))

print("vou terminar em casa")

