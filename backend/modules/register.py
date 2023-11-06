from passlib.hash import pbkdf2_sha512


hash = pbkdf2_sha512.using(rounds=1313, salt_size=5).hash("haha12345")
hash2 = pbkdf2_sha512.using(rounds=1313, salt_size=5).hash("haha123456")
print(hash)
print(hash2)
# print(hash.split('$'))
# print(hash.split('$')[-1])
# print(hash.split('$')[-2])

all = ""

# print(pbkdf2_sha1.verify("haha12345", hash))
