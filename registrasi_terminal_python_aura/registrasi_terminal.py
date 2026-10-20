import json
from pathlib import Path

FILE_DATA = Path(__file__).with_name("data_diri.json")

KOLOM = [
    ("nik", "NIK"),
    ("nama", "Nama lengkap"),
    ("tempat_lahir", "Tempat lahir"),
    ("tanggal_lahir", "Tanggal lahir (DD-MM-YYYY)"),
    ("jenis_kelamin", "Jenis kelamin"),
    ("agama", "Agama"),
    ("status", "Status perkawinan"),
    ("pekerjaan", "Pekerjaan"),
    ("alamat", "Alamat"),
    ("rt", "RT"),
    ("rw", "RW"),
    ("kelurahan", "Kelurahan/Desa"),
    ("kecamatan", "Kecamatan"),
    ("kota", "Kota/Kabupaten"),
    ("kewarganegaraan", "Kewarganegaraan"),
]


def baca_data():
    if not FILE_DATA.exists():
        return []
    try:
        with FILE_DATA.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("\n[!] File data tidak bisa dibaca. Memulai dengan daftar kosong.")
        return []


def simpan_data(data):
    with FILE_DATA.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def garis():
    print("=" * 58)


def judul(teks):
    garis()
    print(teks.center(58))
    garis()


def jeda():
    input("\nTekan Enter untuk kembali ke menu...")


def tambah_data(data):
    judul("REGISTRASI DATA DIRI")
    baru = {}

    for kunci, label in KOLOM:
        while True:
            nilai = input(f"{label}: ").strip()
            if not nilai:
                print("Kolom ini tidak boleh kosong.")
                continue
            if kunci == "nik":
                if not nilai.isdigit() or len(nilai) != 16:
                    print("NIK untuk latihan harus terdiri dari 16 angka.")
                    continue
                if any(item["nik"] == nilai for item in data):
                    print("NIK tersebut sudah terdaftar.")
                    return
            baru[kunci] = nilai
            break

    data.append(baru)
    try:
        simpan_data(data)
    except OSError as error:
        data.pop()
        print(f"\n[!] Gagal menyimpan data: {error}")
        return

    print("\n[✓] Data berhasil disimpan!")
    print(f"Nama: {baru['nama']}")
    print(f"NIK : {baru['nik']}")


def tampilkan_semua(data):
    judul("DAFTAR DATA DIRI")
    if not data:
        print("Belum ada data yang terdaftar.")
        return

    for nomor, item in enumerate(data, start=1):
        print(f"{nomor}. {item['nama']}")
        print(f"   NIK       : {item['nik']}")
        print(f"   Kota      : {item['kota']}")
        print(f"   Pekerjaan : {item['pekerjaan']}")
        print("-" * 58)
    print(f"Jumlah data: {len(data)}")


def tampilkan_detail(item):
    judul("DETAIL DATA DIRI")
    for kunci, label in KOLOM:
        print(f"{label:<30}: {item.get(kunci, '-')}")


def cari_data(data):
    judul("CARI DATA BERDASARKAN NIK")
    nik = input("Masukkan NIK yang ingin dicari: ").strip()
    for item in data:
        if item["nik"] == nik:
            tampilkan_detail(item)
            return
    print("\nData dengan NIK tersebut tidak ditemukan.")


def hapus_data(data):
    judul("HAPUS DATA DIRI")
    nik = input("Masukkan NIK yang ingin dihapus: ").strip()
    for item in data:
        if item["nik"] == nik:
            print(f"Data ditemukan: {item['nama']}")
            konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ").strip().lower()
            if konfirmasi == "y":
                data.remove(item)
                try:
                    simpan_data(data)
                    print("[✓] Data berhasil dihapus.")
                except OSError as error:
                    data.append(item)
                    print(f"[!] Gagal menyimpan perubahan: {error}")
            else:
                print("Penghapusan dibatalkan.")
            return
    print("Data dengan NIK tersebut tidak ditemukan.")


def menu():
    data = baca_data()

    while True:
        print()
        judul("APLIKASI REGISTRASI DATA DIRI")
        print("1. Tambah Data Diri")
        print("2. Lihat Semua Data")
        print("3. Cari Data Berdasarkan NIK")
        print("4. Hapus Data")
        print("5. Keluar")
        garis()

        pilihan = input("Pilih menu [1-5]: ").strip()

        if pilihan == "1":
            tambah_data(data)
            jeda()
        elif pilihan == "2":
            tampilkan_semua(data)
            jeda()
        elif pilihan == "3":
            cari_data(data)
            jeda()
        elif pilihan == "4":
            hapus_data(data)
            jeda()
        elif pilihan == "5":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1 sampai 5.")
            jeda()


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram dihentikan.")
