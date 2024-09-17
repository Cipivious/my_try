import hashlib

# SHA-256
hash_object = hashlib.md5(b'Your data here')
hash_digest = hash_object.hexdigest()
print(hash_digest)

