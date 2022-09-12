teks = input("Masukan Teks!\n")
target = input("Masukan Kata yang ingin dicari!!! \n")

tek = teks.lower().split()
count = 0
for i in tek:
    if i == target.lower():
        count += 1
print("Banyak kata",target,"yang ditemukan adalah",count)