#Metode Bagi Dua

from cmath import e
from tkinter import E

def f(x):
    return x**3-2*x+1

def bagidua(a,b,e):
    step = 1
    print('\n\n===Metode Bagi Dua ===')
    condition = True
    while condition:
        c = (a + b)/2
        print('Iterasi ke-%d, c = %0.6f dan f(c) = %0.6f' % (step, c, f(c)))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        step = step + 1
        condition = abs(f(c)) > e

    print('\nRequired Root is : %0.8f' % c)

a = input('First Guess: ')
b = input('Second Guess: ')
e = input('Toleransi Error: ')

a = float(a)
b = float(b)
e = float(e)


if f(a) * f(b) > 0.0:
    print('Coba dengan perkiraan value yang lain!')
else:
    bagidua(a,b,e)


#Metode Newton Raphson 
def f(x):
    return x**3 - 2*x + 1

def g(x):
    return 3*x**2 - 2


def newtonRaphson(x0,e,N):
    print('\n\n=== Metode Newton Raphson ===')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Turunan tidak boleh = 0')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi ke-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


x0 = input('Masukan Guess: ')
e = input('Toleransi Error: ')
N = input('Maximum Iterasi: ')

x0 = float(x0)
e = float(e)
N = int(N)

newtonRaphson(x0,e,N)