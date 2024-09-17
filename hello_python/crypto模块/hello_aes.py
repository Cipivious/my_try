from Crypto.Cipher import AES 

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce  # 在加密时生成的随机数
ciphertext, tag = cipher.encrypt_and_digest(b'Your data here')

# 解密
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher_dec.decrypt(ciphertext)
print(plaintext.decode())
