nama = input("Masukkan Nama : ")

if nama == "Muhammad":
    print("Selamat Datang Muhammad")
else:
    print("Selamat Datang")
    

umur = int(input("Masukkan Umur : "))

if umur <= 10:
    print("Anda masih kecil")
elif umur >= 10 and umur <= 20:
    print("Anda sudah dewasa")
else:
    print("Anda sudah tua")
    

print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=" + "\n")

angka1 = int(input("Masukkan Angka Pertama : "))
angka2 = int(input("Masukkan Angka Kedua : "))
operator = input("Masukkan Operator (+,-,*,/) : ")

if operator == "+":
    print(angka1 + angka2)
elif operator == "-":
    print(angka1 - angka2)
elif operator == "*":
    print(angka1 * angka2)
elif operator == "/":
    print(angka1 / angka2)
else:
    print("Operator tidak valid")