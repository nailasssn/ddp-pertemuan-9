# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    Fahrenheit=(celcius*9/5)+32
    return Fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)
print('suhu celcius1', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('suhu celcius2', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)


# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 3 == 0 #menentukan bilangan ganjil atau genap
    return hitung #mengembalikan nilai hitung

angka = 4 #mendefinisikan angka yang kita inginkan
hasil = genap_ganjil(angka) #memanggil fungsi
print(f"bilangan{angka} bernilai {hasil}")

angka2 = 9
hasil2 = genap_ganjil(angka2)
print(f"bilangan{angka2} bernilai {hasil2}")

# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
print('## Nomor 3 ##')

def cek_kelulusan(nilai):
    if nilai >= 80:
        return "Lulus"
    else:
        return "Tidak Lulus"

nilai= 80
hasil = cek_kelulusan(nilai)
print(f'nilai {nilai} Adalah: {hasil}')

nilai2= 70
hasil2 = cek_kelulusan(nilai2)
print(f'nilai {nilai2} Adalah: {hasil2}')

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
print('## Nomor 4 ##')
def bilangan_ganjil(number):
  for a in range(1, number, 2):
    print (a, end=" ")

bilangan_ganjil(20)
