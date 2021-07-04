import hashlib


string = input("enter a string")

#md5 algorithm

hash1 = hashlib.md5(string.encode())

#sha256 algorithm

hash2 = hashlib.sha256(string.encode())

# SHA384 algorithm

hash3 = hashlib.sha384(string.encode())

#SHA224 algorithm

hash4 = hashlib.sha224(string.encode())

#SHA512 algorithm

hash5 = hashlib.sha512(string.encode())

#printing all encoded string

print("using md5 algorithm" + " : "+ hash1.hexdigest())
print("using SHA256 algorithm" +" : "+  hash2.hexdigest())
print("using SHA384 algorithm" + " : "+ hash3.hexdigest())
print("using SHA224 algorithm" + " : "+ hash4.hexdigest())
print("using SHA512 algorithm" + " : "+ hash5.hexdigest())

salt = "abc"
salted = salt+string+salt

hash11 = hashlib.md5(salted.encode())
print("using SALTING iteration 1 md5 algorithm" + " : " + hash11.hexdigest())

hash22 = hashlib.md5(str(hash11).encode())
print("iteration 2 " + hash22.hexdigest())

hash33 = hashlib.md5(str(hash22).encode())
print("iteration 3 " + hash33.hexdigest())

hash44 = hashlib.md5(str(hash33).encode())
print("iteration 4 " + hash44.hexdigest())

hash55 = hashlib.md5(str(hash44).encode())
print("iteration 5 " + hash55.hexdigest())


