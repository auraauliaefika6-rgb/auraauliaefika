"""
=====================================================
        PROGRAM MENGHITUNG LUAS SEGITIGA
=====================================================
Rumus : Luas = 0.5 × alas × tinggi
=====================================================
"""


def luas_segitiga(alas: float, tinggi: float) -> float:
    """Menghitung luas segitiga = 0.5 × alas × tinggi"""
    return 0.5 * alas * tinggi


def input_angka(teks: str) -> float:
    """Meminta input angka dari pengguna dengan validasi sederhana."""
    while True:
        try:
            nilai = float(input(teks))
            if nilai <= 0:
                print(">> Nilai harus lebih besar dari 0. Coba lagi.\n")
                continue
            return nilai
        except ValueError:
            print(">> Masukkan harus berupa angka. Coba lagi.\n")


def main():
    print("=" * 45)
    print("       PROGRAM MENGHITUNG LUAS SEGITIGA")
    print("=" * 45)

    a = input_angka("Masukkan panjang alas   : ")
    t = input_angka("Masukkan tinggi segitiga: ")
    hasil = luas_segitiga(a, t)

    print("-" * 45)
    print(f"Alas           : {a}")
    print(f"Tinggi         : {t}")
    print(f"Luas Segitiga  : {hasil:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
