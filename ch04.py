import ecc
import helper

# priv = ecc.PrivateKey(5000)

# print(priv.point.sec(compressed=False).hex())

# priv1 = ecc.PrivateKey(2018**5)

# print(priv1.point.sec(compressed=False).hex())

# priv2 = ecc.PrivateKey(0xdeadbeef12345)

# print(priv2.point.sec(compressed=False).hex())

# priv4 = ecc.PrivateKey(5001)

# print(priv4.point.sec(compressed=True).hex())

# priv5 = ecc.PrivateKey(2019**5)

# print(priv5.point.sec(compressed=True).hex())

# r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
# s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
# sig = ecc.Signature(r, s)
# print(sig.der().hex())

# z = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
# y = 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
# x = 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'

# print(helper.encode_base58(bytes.fromhex(z)))
# print(helper.encode_base58(bytes.fromhex(y)))
# print(helper.encode_base58(bytes.fromhex(x)))

#4.5 
# key1 = 5002
# key2 = 2020**5

# key1 = ecc.PrivateKey(key1)
# key1 = key1.point.address(compressed=False, testnet=True)
# print(key1)

#4.6
# key1 = 5003
# key1 = ecc.PrivateKey(key1).wif(compressed=True, testnet=True)
# print(key1)

#4.9
# bytekey = b'kinjinhanisZZangAndBecomeAKingOfProgramming'#바이트로 된 문자를 인트로 바꾸는 함수 활용해서 비밀키로 만들기위한 전작업
# intkey = helper.little_endian_to_int(bytekey)#바이트 -> 인트
# mykey = ecc.PrivateKey(intkey) # 이러면 이제 256으로 공개된 값을 스칼라곱셈을 해서 공개키가 만들어진다
# print(mykey.point.address(compressed=True, testnet=True))

