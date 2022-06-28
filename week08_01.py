from fractions import Fraction

f=Fraction
number1=f(1,2)
number2=f(13,15)
x=number1+number2

print(f'x={x}')

bunza=(x-number1)
bunmo=(x-1)
y=f(bunza,bunmo)

print(f'y={y}')


