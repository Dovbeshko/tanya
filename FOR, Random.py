from random import randint
list=[randint(1,10) for i in range(10)]
print(list)

a=int(input('Яке число?:'))
n=0
for i in list:
    if i==a:
        n=n+1
if n>=1:
    print(f"Кількість співпадань числа {a} = {n}")
elif n<=a:
    print("Нажаль такого числа немає. Дякую за увагу !!!")
