
data = []
jumlah = int(input("Masukkan jumlah data: "))

for i in range(jumlah):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    data.append(angka)

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print("Data setelah diurutkan (terkecil -> terbesar):", data)
