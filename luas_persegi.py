"""
=====================================================
         PROGRAM MENGHITUNG LUAS PERSEGI
=====================================================
Rumus : Luas = sisi × sisi
=====================================================
"""


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi = sisi × sisi"""
    return sisi ** 2


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
    print("        PROGRAM MENGHITUNG LUAS PERSEGI")
    print("=" * 45)

    s = input_angka("Masukkan panjang sisi persegi : ")
    hasil = luas_persegi(s)

    print("-" * 45)
    print(f"Sisi           : {s}")
    print(f"Luas Persegi   : {hasil:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
