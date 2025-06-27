template = "{num1} {num2}ga bo'linadi"

num = int(input('Son kiriting: '))

if num % 2 == 0:
    print(template.format(num1 = num , num2 = 2))
if num % 3 == 0:
    print(template.format(num1 = num , num2 = 3)) 
if num % 5 == 0:
    print(template.format(num1 = num , num2 = 5))
else:
    print('False')

