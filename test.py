from FNNH import FNNH

print(FNNH(data="test",hash_size=64,rounds=64,returnmode="string",maxreturnval=64))

print(FNNH(data="test",hash_size=65,rounds=64,returnmode="string",maxreturnval=64))

print(FNNH(data="tesb",hash_size=65,rounds=64,returnmode="string",maxreturnval=64))

#=====================================================================================
# from FMEA import FMEA

# plain = "test"

# cipher = FMEA(plain,"testb",mode=1,blocksize=65,stress=1)
# print("encrypted data :",cipher)

# plain = FMEA(cipher,"password",mode=2,blocksize=64,stress=1)
# print("dencrypted data :",plain)

# #=====================================================================================
# import AMKE

# private_rounds = AMKE.generate_rounds()
# print("this is private round:",private_rounds)

# private_key = AMKE.generate_key()
# print("this is private key:",private_key)

# public_key = AMKE.generate_key()
# print("this is public COMMON KEY:",public_key)

# public_key = input("ENTER THE PUBLIC COMMON KEY HERE:")

# print(AMKE.mixkey_phase1(public_key,private_key,private_rounds))

# public_processed_key = input("ENTER THE PUBLIC PROCESSED KEY HERE:")

# print(AMKE.mixkey_phase2(public_processed_key,public_key,private_key,private_rounds))



