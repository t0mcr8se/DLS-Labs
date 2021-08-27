from Crypto.Util.number import getPrime
from sympy.ntheory import isprime as isPrime
from random import randint

def DSA():
    q = getPrime(32)
    # Finding p
    p, i = -1, 2
    while True:
        p = q * i
        if isPrime(p+1):
            break
        i += 1

    # old inefficient code
    # # Finding g
    # g = -1
    # h = randint(2, p-2)
    # for i in range(2, p):
    #     g = i
    #     if pow(g, q, p) == 1 and g == pow(h, (p-1)//q, p):
    #         break

    # Source: https://github.com/ZdrzalikPrzemyslaw/DSA-Key/blob/master/gen_param.py
    h = random.randint(2, p - 2)
    # Compute g:= h^((p-1/q)) % p
    g = pow(h, int((p - 1) // q), p)
    # In the rare case that g=1 try again with a different h
    while g == 1:
        h = random.randint(2, p - 2)
        g = pow(h, int((p - 1) // q), p)

    x = randint(1, q-1)
    y = pow(g, x, p)

    return {
        "public": [p, q, g, y], 
        "private": [p, q, g, x]
    }

