from Crypto.Util.number import long_to_bytes, bytes_to_long


def rsa_fun(p, q, en_text):
    n = p * q
    phi = (p-1) * (q-1)
    d = pow(e, -1, phi)
    e = 3 # TODO: find a better way to generate e

    if type(en_text) is str:
        en_text = en_text.encode()

    elif type(en_text) is not bytes:
        raise Exception("Invalid text encoding")

    ct = bytes_to_long(en_text)
    m = pow(ct, d, n)
    de_text = long_to_bytes(m)


    return (n, e, d, en_text, de_text)







