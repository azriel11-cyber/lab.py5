def tampilkan_menu():
    print("\n" + "="*80)
    print("Program Input Nilai")
    print("="*80)
    print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]: ", end="")

def tampilkan_daftar(data_nilai):
    print("\nDaftar Nilai")
    print("="*80)
    print("| NO |    NIM    |      NAMA      | TUGAS | UTS | UAS | AKHIR |")
    print("="*80)
    
    if not data_nilai:
        print("|" + " "*30 + "TIDAK ADA DATA" + " "*35 + "|")
    else:
        for i, mahasiswa in enumerate(data_nilai, 1):
            akhir = (mahasiswa['tugas'] * 0.3) + (mahasiswa['uts'] * 0.35) + (mahasiswa['uas'] * 0.35)
            print(f"| {i:2} | {mahasiswa['nim']:9} | {mahasiswa['nama']:14} | {mahasiswa['tugas']:5.0f} | {mahasiswa['uts']:3.0f} | {mahasiswa['uas']:3.0f} | {akhir:5.2f} |")
    
    print("="*80)

def tambah_data(data_nilai):
    print("\nTambah Data")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    data_nilai.append({
        'nim': nim,
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas
    })
    print("Data berhasil ditambahkan!")

def ubah_data(data_nilai):
    print("\nUbah Data")
    nim = input("Masukkan NIM yang akan diubah: ")
    
    for mahasiswa in data_nilai:
        if mahasiswa['nim'] == nim:
            print(f"Data ditemukan: {mahasiswa['nama']}")
            mahasiswa['nama'] = input(f"Nama baru [{mahasiswa['nama']}]: ") or mahasiswa['nama']
            mahasiswa['tugas'] = float(input(f"Nilai Tugas baru [{mahasiswa['tugas']}]: ") or mahasiswa['tugas'])
            mahasiswa['uts'] = float(input(f"Nilai UTS baru [{mahasiswa['uts']}]: ") or mahasiswa['uts'])
            mahasiswa['uas'] = float(input(f"Nilai UAS baru [{mahasiswa['uas']}]: ") or mahasiswa['uas'])
            print("Data berhasil diubah!")
            return
    
    print("Data tidak ditemukan!")

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
            return
    
    print("Data tidak ditemukan!")

def cari_data(data_nilai):
    print("\nCari Data")
    nim = input("Masukkan NIM yang dicari: ")
    
    for mahasiswa in data_nilai:
        if mahasiswa['nim'] == nim:
            akhir = (mahasiswa['tugas'] * 0.3) + (mahasiswa['uts'] * 0.35) + (mahasiswa['uas'] * 0.35)
            print("\nData ditemukan:")
            print(f"NIM   : {mahasiswa['nim']}")
            print(f"Nama  : {mahasiswa['nama']}")
            print(f"Tugas : {mahasiswa['tugas']}")
            print(f"UTS   : {mahasiswa['uts']}")
            print(f"UAS   : {mahasiswa['uas']}")
            print(f"Akhir : {akhir:.2f}")
            return
    
    print("Data tidak ditemukan!")

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
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()
