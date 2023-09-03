def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = ""
    for i in message:
        encrypted_msg+=str(pow(ord(i), e, n))+" "
    return encrypted_msg

def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_msg


if __name__=="__main__":
    choice=input("1. Generate keys\n2. Encrypt\n3. Decrypt\nEnter a choice: ")
    if choice=="1":
        p,q=map(int,input("Enter two prime numbers: ").split())
        keys=generate_keys(p,q)
        print("public keys: ", keys[0])
        print("private keys: ",keys[1])
    elif choice=="2":
        text=input("Text to encrypt: ")
        public_key=map(int, input("Enter public key: ").split())
        encrypted_msg=encrypt(text,public_key)
        print(encrypted_msg)
    elif choice=="3":
        ciphertext = list(map(int,input("Enter the ciphertext to decrypt: ").split()))
        private_key = map(int, input("Enter private key: ").split())
        decrypted_msg = decrypt(ciphertext, private_key)
        print("Decrypted Message:", decrypted_msg)
    
