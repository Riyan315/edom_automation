from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Membuka browser...")
driver = webdriver.Chrome()

driver.get("https://igracias.telkomuniversity.ac.id/")

# --- FASE MANUAL ---
print("\n" + "="*50)
print("TUGAS LU SEKARANG:")
print("1. Login manual ke i-GRACIAS.")
print("2. Masuk ke halaman kuesioner sampai Part 1 kebuka.")
print("="*50 + "\n")

input("👉 Tekan ENTER di sini KALAU halaman Part 1 udah kebuka di layar...")

# --- SISTEM LOOPING UNTUK BANYAK PART ---
part_ke = 1

while True:
    print(f"\nMemulai pengisian otomatis untuk Part {part_ke}...")
    
    try:
        # --- BAGIAN 1: ISI RADIO BUTTON ---
        semua_radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
        
        grup_pertanyaan = {}
        for radio in semua_radio:
            nama_grup = radio.get_attribute("name")
            if nama_grup:
                if nama_grup not in grup_pertanyaan:
                    grup_pertanyaan[nama_grup] = []
                grup_pertanyaan[nama_grup].append(radio)
                
        print(f"✅ Ketemu {len(grup_pertanyaan)} pertanyaan pilihan ganda.")
        
        for nama_grup, daftar_opsi in grup_pertanyaan.items():
            jumlah_opsi = len(daftar_opsi)
            if jumlah_opsi == 0:
                continue
                
            if jumlah_opsi == 2:
                indeks_pilihan = 0
            elif jumlah_opsi == 4:
                indeks_pilihan = 2
            elif jumlah_opsi == 5:
                indeks_pilihan = 3
            else:
                indeks_pilihan = jumlah_opsi // 2
                
            driver.execute_script("arguments[0].click();", daftar_opsi[indeks_pilihan])
            time.sleep(0.1)
            
        # --- BAGIAN 2: ISI KOLOM KOMENTAR ---
        kolom_komentar = driver.find_elements(By.TAG_NAME, "textarea")
        if len(kolom_komentar) > 0:
            print(f"✅ Ketemu {len(kolom_komentar)} kolom komentar.")
            for kolom in kolom_komentar:
                kolom.clear() 
                kolom.send_keys(".")
                time.sleep(0.1)
            
        print(f"🎉 Part {part_ke} BERHASIL DIISI!")

    except Exception as e:
        print(f"❌ Ada error pas ngisi: {e}")

    # --- MENU NAVIGASI ---
    print("\n" + "-"*50)
    print("Kalau ada part selanjutnya, klik dulu tombol 'update' atau part berikutnya di web.")
    print("Pilih langkah selanjutnya:")
    print("[1] Lanjut isi lagi (Part selanjutnya)")
    print("[2] Selesai")
    
    pilihan = input("👉 Masukkan angka (1/2) lalu tekan ENTER: ")
    
    if pilihan == '2':
        print("\nSip, pengisian selesai. Jangan lupa klik tombol Simpan terakhir di webnya!")
        break
    elif pilihan == '1':
        part_ke += 1
    else:
        print("\nPilihan gak valid, tapi program tetep nganggep lu mau lanjut ke part berikutnya...")
        part_ke += 1

# Kasih waktu bentar sebelum nutup biar lu bisa submit manual
input("\nTekan ENTER untuk menutup browser dan mematikan program...")
driver.quit()