import encrypt_decrypt as enc_dec


string_ = input("Write your message: ")
key = int(input("Write your key: "))

encrypted_str = (enc_dec.encrypt(string_, key))
print(encrypted_str)

decrypted_str = (enc_dec.decrypt(encrypted_str, key))
print(decrypted_str)
