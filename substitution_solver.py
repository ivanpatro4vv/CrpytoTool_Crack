import string 

plaintext = 'SELAMAT DATANG DI KELAS KRIPTOGRAFI'
cipheralphabet = 'QAMOCDBHRUWLKJNVTZFISPEGYX'
plainalphabet = string.ascii_uppercase

def encrypt(plaintext,cipheralphabet):
    ciphertext = ''
    for p in plaintext:
        if p == ' ':
            c = ' '
        else: c = cipheralphabet[plainalphabet.index(p)]
        ciphertext +=c
    return ciphertext

def decrypt(ciphertext,cipheralphabet):
    plaintext = ''
    for c in ciphertext:
        if c == ' ':
            p = ' '
        else: p = plainalphabet[cipheralphabet.index(c)]
        plaintext += p
    return plaintext

ciphertext = encrypt(plaintext,cipheralphabet)
print(ciphertext)
print(decrypt(ciphertext,cipheralphabet))
