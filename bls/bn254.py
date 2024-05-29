from mcl import G1, G2;

class BN254:
  def __init__():
    return;

G2_XA = 0x1800deef121f1e76426a00665e5c4479674322d4f75edadd46debd5cd992f6ed
G2_XB = 0x198e9393920d483a7260bfb731fb5d25f1aa493335a9e71297e485b7aef312c2
G2_YA = 0x12c85ea5db8c6deb4aab71808dcb408fe3d1e7690c43d37b4ce6cc0166fa7daa
G2_YB = 0x090689d0585ff075ec9e99ad690c3395bc4b313370b38ef355acdadcd122975b


BN254.G1 = G1()
BN254.G1.setStr(b"1 1 2")

BN254.G2 = G2()
BN254.G2.setStr(f"1 {G2_XA} {G2_XB} {G2_YA} {G2_YB}".encode("utf-8"))

