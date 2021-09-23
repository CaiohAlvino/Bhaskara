
import math
a = float(input('qual é o valor de a?'))
b = float(input('qual é o valor de b?'))
c = float(input('qual é o valor de c?'))

delta = (b ** 2) - (4 * a * c)

print('                 ')
print('                 ')

if delta < 0 :
        print ("Raiz negativa nao pode ser extraida.")
        exit()
 
else :
    x=math.sqrt(delta)
    x1=(-b - x) / (2 * a)
    x2=(-b + x) / (2 * a)
    
print('x1: {}, x2: {}'.format(x1, x2))