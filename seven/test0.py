from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        ## !- means *if not equal*
        print(f"ERRORd on is_prime({n}, expected {expected}")