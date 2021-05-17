import ecc

priv = ecc.PrivateKey(5000)

print(priv.point.sec(compressed=False).hex())

priv1 = ecc.PrivateKey(2018**5)

print(priv1.point.sec(compressed=False).hex())

priv2 = ecc.PrivateKey(0xdeadbeef12345)

print(priv2.point.sec(compressed=False).hex())

priv4 = ecc.PrivateKey(5001)

print(priv4.point.sec(compressed=True).hex())

priv5 = ecc.PrivateKey(2019**5)

print(priv5.point.sec(compressed=True).hex())