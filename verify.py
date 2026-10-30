"""
verify.py - cross-checks the ancient-method code against modern functions:
(1) a fixed list of worked examples, and (2) 1000 random tests per algorithm.
Run:  python verify.py
"""
import random
from ancient_algorithms import kuttaka_modular_inverse, aryabhata_square_root, aryabhata_cube_root
from modern_checks import modern_inverse, modern_sqrt, modern_cbrt

random.seed(2026)

print("=== Kuttaka / Modular Inverse ===")
for b, a in [(45, 157), (91, 1000), (123, 2026)]:
    inv, steps = kuttaka_modular_inverse(b, a)
    print(f"b={b}, a={a} -> ancient={inv}, modern={modern_inverse(b, a)}, "
          f"match={inv == modern_inverse(b, a)}, steps={len(steps)}")

print("\n=== Square Root (Varga) ===")
for n in [4782969, 1000000007, 2147395600, 99, 10**12]:
    r, rem, steps = aryabhata_square_root(n)
    print(f"n={n} -> ancient={r}, modern={modern_sqrt(n)}, "
          f"match={r == modern_sqrt(n)}, remainder={rem}")

print("\n=== Cube Root (Ghana) ===")
for n in [12812904, 1000000007, 74088, 2**30, 999999999999]:
    r, rem, steps = aryabhata_cube_root(n)
    print(f"n={n} -> ancient={r}, modern={modern_cbrt(n)}, "
          f"match={r == modern_cbrt(n)}, remainder={rem}")

print("\n=== Random stress test (1000 inputs per algorithm) ===")
ok_k = ok_s = ok_c = 0
for _ in range(1000):
    a = random.randint(2, 10**6)
    b = random.randint(1, a - 1)
    try:
        inv, _ = kuttaka_modular_inverse(b, a)
        ok_k += (inv == modern_inverse(b, a))
    except ValueError:      # gcd != 1: no inverse; modern pow() must also fail
        try:
            modern_inverse(b, a)
        except ValueError:
            ok_k += 1
    n = random.randint(1, 10**15)
    ok_s += (aryabhata_square_root(n)[0] == modern_sqrt(n))
    ok_c += (aryabhata_cube_root(n)[0] == modern_cbrt(n))
print(f"Kuttaka     : {ok_k}/1000 matched the modern result")
print(f"Square root : {ok_s}/1000 matched the modern result")
print(f"Cube root   : {ok_c}/1000 matched the modern result")
