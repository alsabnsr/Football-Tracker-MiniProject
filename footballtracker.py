JumlahMatch = int(input("Jumlah Pertandingan: "))

for i in range(JumlahMatch):
    SkorKita = int(input("Skor tim kita: "))
    SkorLawan = int(input("Skor tim lawan: "))

    if SkorKita > SkorLawan:
        print("Menang")
    elif SkorKita == SkorLawan:
        print("Seri")
    else:
        print("Kalah")