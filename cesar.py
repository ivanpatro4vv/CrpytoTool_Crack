def cesar_decrypt(ciphertext, shift):
    decrypted = ''.join(chr((ord(c) - 97 - shift) % 26 + 97) for c in ciphertext)
    return decrypted

ciphertext = "khoor"  # Exemple de texte chiffré avec un décalage de 3 (Hello)
shift = 3
print(f'Decrypted message: {cesar_decrypt(ciphertext, shift)}')
