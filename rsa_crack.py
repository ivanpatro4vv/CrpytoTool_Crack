from Crypto.PublicKey import RSA
from Crypto.Util import number
import math

# RSA weak key: n = p * q
# Example n = 3233 (public key modulus)
n = 3233
e = 3  # public exponent

def find_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None

def rsa_decrypt(n, e, c):
    p, q = find_factors(n)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    return m

# Example ciphertext (encrypted message)
ciphertext = 2209

# Decrypt the message
message = rsa_decrypt(n, e, ciphertext)
print(f'Decrypted message: {message}')
