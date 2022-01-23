#importando somente a função de raiz quadrada, usando o from
#importar numeros aleatorios usar a biblioteca Random 
# randonint gerar numero aleatorio inetiro
#from  math import trunc
#num = float (input("digite um numero: "))
#print("O numero  digitado foi {} é a porção inteira é {}".format(num, math.trunc(num)))'''
'''import math
cato = float(input("digite o comprimento do cateto oposto :"))
cata = float(input("digite o comprimento do cateto adjacente: "))
hipo = math.hypot(cato,cata)
print("A hipotenusa vai medir {:2f}".format(hipo))'''

import math
ang = float(input("Digite um angulo: "))
seno = math.sin(math.radians(ang))
print("O angulo de {} tem o SENO de {:.2f}".format(ang,seno))
cosseno = math.cos(math.radians(ang))
print("O angulo de {} tem o COSSENO de {:.2f}".format(ang,cosseno))
tang = math.tan(math.radians(ang))
print("O angulo de {} tem a TANGENTE de {:.2f}".format (ang,tang))







