import ecc

priv = ecc.PrivateKey(5000)

print(priv.point.sec().hex())

priv1 = ecc.PrivateKey(2018**5)

print(priv1.point.sec().hex())