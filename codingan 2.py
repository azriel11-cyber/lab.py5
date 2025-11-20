def tampilkan_menu():
    print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:", end="")

def tampilkan_daftar(data_nilai):
    print("\nDaftar Nilai")
    print("="*75)
    print("| NO |   NIM   |     NAMA      | TUGAS | UTS | UAS | AKHIR |")
    print("="*75)
    
    if not data_nilai:
        print("|" + " "*27 + "TIDAK ADA DATA" + " "*32 + "|")
    else:
        for i, mahasiswa in enumerate(data_nilai, 1):
            akhir = (mahasiswa['tugas'] * 0.3) + (mahasiswa['uts'] * 0.35) + (mahasiswa['uas'] * 0.35)
            print(f"| {i:2} | {mahasiswa['nim']:7} | {mahasiswa['nama']:13} | {mahasiswa['tugas']:5} | {mahasiswa['uts']:3} | {mahasiswa['uas']:3} | {akhir:5.2f} |")
    
    print("="*75)

def tambah_data(data_nilai):
    print("\nTambah Data")
    nim = input("NIM         : ")
    nama = input("Nama        : ")
    uts = int(input("Nilai UTS   : "))
    uas = int(input("Nilai UAS   : "))
    tugas = int(input("Nilai Tugas : "))
    
    data_nilai.append({
        'nim': nim,
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas
    })

def ubah_data(data_nilai):
    print("\nUbah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    
    for mahasiswa in data_nilai:
        if mahasiswa['nim'] == nim:
            print(f"\nData ditemukan: {mahasiswa['nama']}")
            nama = input(f"Nama baru [{mahasiswa['nama']}]: ")
            uts = input(f"Nilai UTS baru [{mahasiswa['uts']}]: ")
            uas = input(f"Nilai UAS baru [{mahasiswa['uas']}]: ")
            tugas = input(f"Nilai Tugas baru [{mahasiswa['tugas']}]: ")
            
            if nama: mahasiswa['nama'] = nama
            if uts: mahasiswa['uts'] = int(uts)
            if uas: mahasiswa['uas'] = int(uas)
            if tugas: mahasiswa['tugas'] = int(tugas)
            
            print("Data berhasil diubah!")
            return
    
    print("Data dengan NIM tersebut tidak ditemukan!")

def hapus_data(data_nilai):
    print("\nHapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ")
    
    for i, mahasiswa in enumerate(data_nilai):
        if mahasiswa['nim'] == nim:
            print(f"Data ditemukan: {mahasiswa['nama']}")
            konfirmasi = input("Yakin ingin menghapus? (y/n): ")
            if konfirmasi.lower() == 'y':
                data_nilai.pop(i)
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan!")
            return
    
    print("Data dengan NIM tersebut tidak ditemukan!")

def cari_data(data_nilai):
    print("\nCari Data")
    nim = input("Masukkan NIM yang dicari: ")
    
    for mahasiswa in data_nilai:
        if mahasiswa['nim'] == nim:
            akhir = (mahasiswa['tugas'] * 0.3) + (mahasiswa['uts'] * 0.35) + (mahasiswa['uas'] * 0.35)
            print("\nData ditemukan:")
            print(f"NIM         : {mahasiswa['nim']}")
            print(f"Nama        : {mahasiswa['nama']}")
            print(f"Nilai UTS   : {mahasiswa['uts']}")
            print(f"Nilai UAS   : {mahasiswa['uas']}")
            print(f"Nilai Tugas : {mahasiswa['tugas']}")
            print(f"Nilai Akhir : {akhir:.2f}")
            return
    
    print("Data dengan NIM tersebut tidak ditemukan!")

def main():
    data_nilai = []
    
    while True:
        tampilkan_menu()
        pilihan = input().lower()
        
        if pilihan == 'l':
            tampilkan_daftar(data_nilai)
        elif pilihan == 't':
            tambah_data(data_nilai)
        elif pilihan == 'u':
            ubah_data(data_nilai)
        elif pilihan == 'h':
            hapus_data(data_nilai)
        elif pilihan == 'c':
            cari_data(data_nilai)
        elif pilihan == 'k':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
