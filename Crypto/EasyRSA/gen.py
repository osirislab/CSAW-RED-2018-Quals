import rsa
import binascii

flag = "flag{R0n_Adi_&_Leo_wou1d_b3_pr0ud}"
(pub, priv) = rsa.newkeys(512)
flag_num = int(binascii.hexlify(bytes(flag,'utf8')), 16)
cipher = pow(flag_num, pub.e, pub.n)
private = pow(cipher, priv.d, priv.n)
print("N =", priv.n)
print("d =", priv.d)
print("c =",cipher)
