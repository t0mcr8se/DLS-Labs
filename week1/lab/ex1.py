

def getKey(p, q, e=3):
    n = p * q
    phi = (p-1) * (q-1)
    d = pow(e, -1, phi)

    return (n, e, d)

print(getKey(53, 59))




