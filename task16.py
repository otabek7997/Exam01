price = 100_000
age = int(input('Yoshingizni kiriting: '))

if age <=7:
    discount = 50
if 7 < age <= 14:
    discount = 20
if age > 14:
    discount = 10

yakuniy_narx = price - ((price * discount) / 100)

print('Yakuniy narx:', yakuniy_narx , (discount ,'foiz chegirma bilan'))