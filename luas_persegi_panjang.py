"""
=====================================================
      PROGRAM MENGHITUNG LUAS PERSEGI PANJANG
=====================================================
Rumus : Luas = panjang × lebar
=====================================================
"""


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang = panjang × lebar"""
    return panjang * lebar


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
    print("=" * 48)
    print("     PROGRAM MENGHITUNG LUAS PERSEGI PANJANG")
    print("=" * 48)

    p = input_angka("Masukkan panjang : ")
    l = input_angka("Masukkan lebar   : ")
    hasil = luas_persegi_panjang(p, l)

    print("-" * 48)
    print(f"Panjang              : {p}")
    print(f"Lebar                : {l}")
    print(f"Luas Persegi Panjang : {hasil:.2f}")
    print("=" * 48)


if __name__ == "__main__":
    main()
