import sqlite3  # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db")  # Tabloya bağlanıyoruz.

# cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
cursor = con.cursor()


def tablo_oluştur():
    # Sorguyu çalıştırıyoruz.
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
    con.commit()


tablo_oluştur()
con.close()  # Bağlantıyı koparıyoruz.
