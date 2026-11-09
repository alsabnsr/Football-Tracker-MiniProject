JumlahMatch = int(input("Jumlah Pertandingan: "))

menang = 0
seri = 0
kalah = 0

TotalGol = 0
TotalKebobolan = 0

TotalPoin = 0

ListSkorKita = []
ListSkorLawan = []

if JumlahMatch <= 0:
    print("Tidak Ada Match")
else:
    for i in range(JumlahMatch):
        SkorKita = int(input("Skor tim kita: "))
        SkorLawan = int(input("Skor tim lawan: "))

        ListSkorKita.append(SkorKita)
        ListSkorLawan.append(SkorLawan)

        if SkorKita > SkorLawan:
            menang = menang + 1
            TotalPoin = TotalPoin + 3
        elif SkorKita == SkorLawan:
            seri = seri + 1
            TotalPoin = TotalPoin + 1
        else:
            kalah = kalah + 1
            TotalPoin = TotalPoin + 0

        TotalGol = TotalGol + SkorKita
        TotalKebobolan = TotalKebobolan + SkorLawan

    RataRataGol = TotalGol / JumlahMatch
    RataRataKebobolan = TotalKebobolan / JumlahMatch

    print("Menang:", menang)
    print("Seri:", seri)
    print("Kalah:", kalah)
    print("Total Poin: ", TotalPoin)
    print("Total Gol:", TotalGol)
    print("Total Kebobolan:", TotalKebobolan)
    print("Rata-rata Gol:", RataRataGol)
    print("Rata-rata Kebobolan:", RataRataKebobolan)
    print("Skor Kita: ", ListSkorKita)
    print("Skor Lawan: ", ListSkorLawan)

    print("===Riwayat Pertandingan===")
    for i in range(JumlahMatch):
        print("Match ke-",i+1,":", ListSkorKita[i], "-", ListSkorLawan[i])