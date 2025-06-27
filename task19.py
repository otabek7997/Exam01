matn = input("Matn kiriting: ")
unlilar = ['a','e','i','o','u']
sana = 0

for harf in matn:
    if harf in unlilar:
        sana += 1

print(sana)
  