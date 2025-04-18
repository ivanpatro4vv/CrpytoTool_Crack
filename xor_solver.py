def xor_decrypt(ciphertext, key):
    return ''.join(chr(c ^ key) for c in ciphertext)

# Exemple de message chiffré (XOR avec une clé)
ciphertext = [100, 200, 50, 170]  # exemple de texte chiffré

# Tester toutes les clés possibles
for key in range(256):
    
    decrypted = xor_decrypt(ciphertext, key)
    print(f'Key: {key}, Decrypted message: {decrypted}')
