"""
=====================================================
        PROGRAM MENGHITUNG LUAS LINGKARAN
=====================================================
Rumus : Luas = π × r²
=====================================================
"""

import math


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran = π × r²"""
    return math.pi * jari_jari ** 2


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
    print("      PROGRAM MENGHITUNG LUAS LINGKARAN")
    print("=" * 45)

    r = input_angka("Masukkan jari-jari lingkaran : ")
    hasil = luas_lingkaran(r)

    print("-" * 45)
    print(f"Jari-jari      : {r}")
    print(f"Luas Lingkaran : {hasil:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()
