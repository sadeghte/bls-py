import mcl;
import os
from .bn254 import BN254;


class KeyPair:
  def __init__(self, secret: bytes=b""):
    self.secret = mcl.Fr()
    if not secret:
      self.secret.setHashOf(os.urandom(64))
    else:
      self.secret.setStr(secret)

    self.pub_G1 = (BN254.G1 * self.secret).normalize()
    self.pub_G2 = (BN254.G2 * self.secret).normalize()

  def encode_secret(self) -> bytes:
    return self.secret.getStr()