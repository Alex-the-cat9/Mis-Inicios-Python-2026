from hashlib import sha256
hash_final = sha256("gato".encode()).hexdigest()
print(hash_final)
#probando otra vez sha-256