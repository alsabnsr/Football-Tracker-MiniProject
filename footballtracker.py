JumlahMatch = int(input("Jumlah Pertandingan: "))

menang = 0
seri = 0
kalah = 0

TotalGol = 0
TotalKebobolan = 0

for i in range(JumlahMatch):
    SkorKita = int(input("Skor tim kita: "))
    SkorLawan = int(input("Skor tim lawan: "))

    if SkorKita > SkorLawan:
        menang = menang + 1
    elif SkorKita == SkorLawan:
        seri = seri + 1
    else:
        kalah = kalah + 1

    TotalGol = TotalGol + SkorKita
    TotalKebobolan = TotalKebobolan + SkorLawan

RataRataGol = TotalGol / JumlahMatch
RataRataKebobolan = TotalKebobolan / JumlahMatch

print("Menang:", menang)
print("Seri:", seri)
print("Kalah:", kalah)
print("Total Gol:", TotalGol)
print("Total Kebobolan:", TotalKebobolan)
print("Rata-rata Gol:", RataRataGol)
print("Rata-rata Kebobolan:", RataRataKebobolan)