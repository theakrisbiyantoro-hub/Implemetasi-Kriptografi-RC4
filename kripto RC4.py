def KSA(key):
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def PRGA(S, length):
    i = 0
    j = 0
    keystream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    return keystream


def encrypt(key, plaintext):
    S = KSA(key)
    keystream = PRGA(S, len(plaintext))

    ciphertext = []

    for i in range(len(plaintext)):
        c = ord(plaintext[i]) ^ keystream[i]
        ciphertext.append(c)

    return ciphertext


def decrypt(key, ciphertext):
    S = KSA(key)
    keystream = PRGA(S, len(ciphertext))

    plaintext = ""

    for i in range(len(ciphertext)):
        p = ciphertext[i] ^ keystream[i]
        plaintext += chr(p)

    return plaintext


# =====================
# MAIN PROGRAM
# =====================

key = input("Masukkan key: ")
plaintext = input("Masukkan plaintext: ")

cipher = encrypt(key, plaintext)

print("\nCiphertext (HEX):")
print(' '.join(hex(c) for c in cipher))

decrypted = decrypt(key, cipher)

print("\nHasil dekripsi:")
print(decrypted)