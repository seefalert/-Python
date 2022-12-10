# a = int(input())
# if  a%10==2 and a%100 != 12:
#     print(a, 'программиста')
# elif a % 10 == 3 and a % 100 != 13:
#     print(a, 'программиста')
# elif a % 10 == 4 and a % 100 != 14:
#     print(a, 'программиста')
# elif a%10==1 and a% 100!=11:
#     print(a, 'программист')
# else:
#     print(a, 'программистов')

# a=int(input())
# q,w,e,r,t,y=a//100000,a//10000%10,a//1000%10,a//100%10,a//10%10,a//1%10
# if (q+w+e)!=(r+t+y):
#     print('Обычный')
# else:
#     print('Счастливый')
# or
# a, b, c, d, e, f = input()
# n= int(a)+int (b)+int(c)
# m= int(d)+int (e)+int(f)
# if n==m:
#     print ('Счастливый')
# else:
#     print ('Обычный')

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#
# Пример 3 с комментариями:
#
# a = int(input()) # задаем значение a
# b = int(input()) # задаем значение b
# s = 0            # принимаем сумму изначально равной 0
# i = a            # в качестве i вводим переменную, которая на i-м шаге равна i-му целому числу на отрезке
# while i <= b:    # цикл работает, пока i-е число не станет равно верхнему значению отрезка
#     s += i       # на каждом шаге сумма увеличивается на i-е число
#     i += 1       # шаг - единица (рассматриваем каждый раз следующее целое число)
# print(s)


# a,b=int(input()),0
# while a!=0:
#     b = b + a
#     a=int(input())
# print(b)

# a = int(input())
# b = int(input())
# c=a
# while a % b:
#     a+=c
# print(a)


# a = 0
# q = 1
# while q:
#     a = int(input())
#     if a > 100:
#         break
#     elif a >= 10:
#         print(a)


# q,w,e,r = int(input()),int(input()),int(input()),int(input())
# for j in range(e,r+1):
#     print('\t', j, end='')
# print()
# for y in range(q,w+1):
#     print(y,end='\t')
#     for i in range(e,r+1):
#         print(i*y, end='\t')
#     print()


# a,b = input().split()
# a,b,s=int(a),int(b),0
# for i in range(a,b+1):
#     if i % 2 ==1:
#         s+=i
# print(s)
# //
# a,b = input().split()
# a,b,s=int(a),int(b),0
# if a % 2 == 0:
#     a += 1
# for i in range(a,b+1,2):
#     s += i
# print(s)
# //
# a,b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a,b+1,2):
#     s += i
# print(s)


# a,b = int(input()),int(input())
# s,n=0,0
# for i in range(a,b+1):
#     if i % 3 == 0:
#         s += i
#         n += 1
# print(s/n)
# //
# x=[x for x in range(int(input()),int(input())+1) if x % 3 == 0]
# print(sum(x)/len(x))
# x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
# генерируется список и присваивается переменной х. Такая штука называется "list comprehension".
# Устроено это следующим образом:
# 1. квадратные скобки говорят нам о том, что создаеся список.
# 2. "x for x in range(int(input()),int(input()) + 1)"  --  перебираются все значения х на вводимом интервале "(int(input()),int(input()) + 1)", где +1 позволяет включить в интервал верхнюю вводимую границу
# 3. условие  "if x % 3 == 0" говорить о том, что в наш список попадут только те значения х, которые кратны 3.
#
# В строке
# print(sum(x)/len(x))
# функция sum(x) возвращает результат сложения всех элементов списка х,
# а функция len(x) - количество элементов в этом списке.


# a=int(input())
# b=int(input())
# c=int(input())
# list=[a,b,c]
# q=max(list)
# w=min(list)
# e=(a+b+c)-(q+w)
# print(q)
# print(w)
# print(e)


# a,b,c=int(input()),int(input()),int(input())
# q,w=max(a,b,c),min(a,b,c)
# e=(a+b+c)-(q+w)
# print(q,w,e, sep="\n")


# a=str(input())
# b=int(input())
# pi=3.14
# if a == 'треугольник':
#     q = int(input())
#     c = int(input())
#     p = (b + c + q) / 2
#     s = (p * (p - q) * (p - b) * (p - c))
#     print(s ** 0.5)
# elif a == 'прямоугольник':
#     c = int(input())
#     print(b*c)
# elif a == 'круг':
#     print(pi*b**2)


# a=float(input())
# b=float(input())
# c=str(input())
# if c =='+':
#     print(a + b)
# elif c =='-':
#     print(a - b)
# elif c=='/':
#     if a == 0.0 or b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
# elif c == '*':
#     print(a * b)
# elif c == 'mod':
#     if a == 0.0 or b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif c == 'pow':
#     print(a ** b)
# elif c == 'div':
#     if a == 0.0 or b == 0.0:
#         print('Деление на 0!')
#     else:
#         print(a // b)


# a = str(input().lower())
# G, C = a.count('g'), a.count('c')
# print(((G + C) / (len(a)))*100)
# //
# s = input().upper()
# print((s.count('G') + s.count('C'))/len(s) * 100)


# s = str(input())
# n,q = 1,1
# for i in s:
#     if len(s)==n:
#         print(s[-1],q, sep='', end='')
#     elif s[n] == i:
#         q+=1
#     else:
#         print(i,q, sep='', end='')
#         q=1
#     n += 1


# f=[int(i) for i in input().split()]
# print(sum(f))


# f=[int(i) for i in input().split()]
# m,n = -1,1
# for s in f:
#     if len(f)==1:
#         print(f[0])
#         break
#     elif len(f)==n:
#         print(f[0]+f[m], end=' ')
#         break
#     print(f[n]+f[m],end=' ')
#     n += 1
#     m += 1























































































































































































