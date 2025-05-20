def gcd_iterative(a, b):

    while b:
        a, b = b, a % b
        print(f"gcd({a},{b}) = gcd({b}, {a} mod {b})")
    return a

bil1 = int(input("Masukan Nilai Bilangan Pertama (a) : ")
bil2 = int(input("Masukan Nilai Bilangan Kedua (b) : ")
           
print(f"GCD({bil1},{bil2} ) = {gcd_iterative(bil1, bil2)}")
