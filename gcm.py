def gcd_iterative(a, b):
    """
    Menghitung GCD (FPB) dari dua bilangan bulat menggunakan algoritma Euclidean iteratif.

    Args:
        a: Bilangan bulat pertama.
        b: Bilangan bulat kedua.

    Returns:
        GCD dari a dan b.
    """
    while b:  # Selama b bukan nol
        a, b = b, a % b  # Ganti a dengan b, dan b dengan sisa bagi a % b
        print(f"gcd({a},{b}) = gcd({b}, {a} mod {b})")
    return a

print(f"GCD(101, 103) = {gcd_iterative(101, 103)}") # Output: GCD(101, 103) = 1 (bilangan prima relatif)
