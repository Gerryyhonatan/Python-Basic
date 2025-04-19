for i in range(5,10):
    print(i)
    
angka = [1,2,3,4,5]

for i in angka:
    print(f"i sekarang adalah -> {i}")
    
angka = 10

while angka < 20:
    print(f"angka sekarang adalah -> {angka}")
    angka += 1

# For 
sisi = 5
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# While
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
    
sisi = 7
count = 1
spasi = int(sisi/2)

while True:
    if(count % 2):
        print(" "*spasi + "+"*count)
        count += 1
        spasi -= 1
    else: 
        count += 1
        continue
    
    if count > sisi:
        break
    
count = sisi - 2
spasi = 1

while count > 0:
    if count % 2:
        print(" " * spasi + "+" * count)
        spasi += 1
    count -= 1