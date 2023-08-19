import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()


def tablo_olustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()


def deger_ekle(isim, yazar, yayınevi, sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",
                   (isim, yazar, yayınevi, sayfa_sayısı))
    con.commit()


def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def verileri_al3(yayınevi):
    # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    cursor.execute("Select * From kitaplık where Yayınevi = ?", (yayınevi,))
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


verileri_al3("Everest")
con.close()
