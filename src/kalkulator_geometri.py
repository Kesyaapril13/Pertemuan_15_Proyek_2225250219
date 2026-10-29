import math


def persegi(sisi):
    """Menghitung luas dan keliling persegi."""
    if sisi <= 0:
        raise ValueError("Sisi harus lebih dari 0.")

    luas = sisi ** 2
    keliling = 4 * sisi

    return luas, keliling


def persegi_panjang(panjang, lebar):
    """Menghitung luas dan keliling persegi panjang."""
    if panjang <= 0 or lebar <= 0:
        raise ValueError(
            "Panjang dan lebar harus lebih dari 0."
        )

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    return luas, keliling


def segitiga(alas, tinggi, sisi_a, sisi_b, sisi_c):
    """Menghitung luas dan keliling segitiga."""
    if alas <= 0 or tinggi <= 0:
        raise ValueError(
            "Alas dan tinggi harus lebih dari 0."
        )

    if min(sisi_a, sisi_b, sisi_c) <= 0:
        raise ValueError("Semua sisi harus lebih dari 0.")

    if (
        sisi_a + sisi_b <= sisi_c
        or sisi_a + sisi_c <= sisi_b
        or sisi_b + sisi_c <= sisi_a
    ):
        raise ValueError(
            "Ketiga sisi tidak membentuk segitiga."
        )

    luas = 0.5 * alas * tinggi
    keliling = sisi_a + sisi_b + sisi_c

    return luas, keliling


def lingkaran(jari_jari):
    """Menghitung luas dan keliling lingkaran."""
    if jari_jari <= 0:
        raise ValueError(
            "Jari-jari harus lebih dari 0."
        )

    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari

    return luas, keliling
