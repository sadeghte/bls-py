import mcl;
from .bn254 import BN254;
from .key_pair import KeyPair;
from Crypto.Hash import keccak



# modulus for the underlying field F_p of the elliptic curve
FP_MODULUS = 21888242871839275222246405745257275088696311157297823662689037894645226208583
# modulus for the underlying field F_r of the elliptic curve
FR_MODULUS = 21888242871839275222246405745257275088548364400416034343698204186575808495617

FIELD_ORDER = 0x30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd47

# convert bytes to args
def b2x(_bytes: bytes) -> str:
  # result = _bytes.decode("utf-8")
  # if len(result) % 2 == 1:
  #   result = "0" + result
  # return "0x" + result

  return int(_bytes, 16)

def point_G1(x: int, y: int) -> mcl.G1:
  result = mcl.G1()
  result.setStr(f"1 {x} {y}".encode("utf-8"))
  return result

def addmod(a, b, m):
  return (a + b) % m

def mulmod(a, b, m):
  return(a * b) % m

def expmod(a, b, m):
  result = 1
  base = a
  _b = b
  while _b > 0:
    # Check the least significant bit (LSB) of b
    if _b & 1:
      result = (result * base) % m
    # Right shift b by 1 (effectively dividing by 2, discarding the remainder)
    _b >>= 1
    # Square the base for the next iteration (efficient for repeated multiplication)
    base = (base * base) % m
  return result

class BLS:

  @staticmethod
  def create_key_pair(secret: bytes = b"") -> KeyPair:
    return KeyPair(secret)
  
  @staticmethod
  def hash_str(input_string: str) -> bytes:
    k = keccak.new(digest_bits=256)
    k.update(input_string.encode())
    # return k.hexdigest() # return hex string
    return k.digest()
  
  @staticmethod
  def map_to_g1(hash: bytes) -> mcl.G1:
    return mcl.G1.hashAndMapTo(hash).normalize()

  @staticmethod
  def sign_short(message: bytes, key_pair: KeyPair) -> mcl.G1:
    hash_value = BLS.hash_to_G1(message)
    return(hash_value * key_pair.secret).normalize()

  @staticmethod
  def verify_short(message: bytes, signature: mcl.G1, pub_key: mcl.G2) -> bool:
    hash_value = BLS.hash_to_G1(message)
    gt1 = mcl.GT.pairing(hash_value, pub_key)
    gt2 = mcl.GT.pairing(signature, BN254.G2)
    return gt1 == gt2
  
  @staticmethod
  def hash_to_G1(_x: bytes) -> mcl.G1:
    beta = 0
    y = 0
    x = int.from_bytes(_x, "big") % FP_MODULUS
    while True:
        (beta, y) = BLS.find_y_from_x(x)
        # y^2 == beta
        if( beta == ((y * y) % FP_MODULUS) ):
            return point_G1(x, y)
        x = (x + 1) % FP_MODULUS
    return point_G1(0, 0)

  @staticmethod
  def find_y_from_x(x: int) -> 'tuple[int, int]':
    # beta = (x^3 + b) % p
    beta = addmod(mulmod(mulmod(x, x, FP_MODULUS), x, FP_MODULUS), 3, FP_MODULUS)
    # y^2 = x^3 + b
    # this acts like: y = sqrt(beta) = beta^((p+1) / 4)
    y = expmod(beta, 0xc19139cb84c680a6e14116da060561765e05aa45a1c72a34f082305b61f3f52, FP_MODULUS)
    return (beta, y)
  
  @staticmethod
  def aggregate_points(points):
    agg = points[0]
    for p in points[1:]:
      agg = agg + p
    return agg.normalize()

  
  @staticmethod
  def g1_to_args(point: mcl.G1) -> dict:
    return {
      "X": b2x(point.getX().getStr(16)),
      "Y": b2x(point.getY().getStr(16))
    }
  
  @staticmethod
  def g2_to_args(point: mcl.G1) -> dict:
    return {
      "X": [b2x(point.getX().get_a().getStr(16)), b2x(point.getX().get_b().getStr(16))],
      "Y": [b2x(point.getY().get_a().getStr(16)), b2x(point.getY().get_b().getStr(16))]
    }