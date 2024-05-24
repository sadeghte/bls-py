import unittest
from bls import BLS
from bls.bn254 import BN254
from web3 import Web3
from .consts import VERIFIER_CONTRACT_ABI


class EthereumContractTestCase(unittest.TestCase):
  def setUp(self):
    # Connect to an Ethereum node
    # self.web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))
    self.web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s2.binance.org:8545'))
    # self.web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-2-s1.binance.org:8545'))
    # self.web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-2-s2.binance.org:8545'))

    # Set up the contract
    contract_address = '0x588991F235046d67a60b8fd6682Ac7A1B34e8a2b'

    self.contract = self.web3.eth.contract(
      address=contract_address,
      abi=VERIFIER_CONTRACT_ABI
    )
    # Ensure that you are connected
    assert self.web3.is_connected()


  def test_contract_verification(self):
    """Simple signature should verify by contract"""
    
    key_pair = BLS.create_key_pair()
    message = BLS.hash_str("Hello, World!")
    signature = BLS.sign_short(message, key_pair)

    # Call a contract function
    [pairingSuccessful, siganatureIsValid] = self.contract.functions.verifySignature(
      # message
      message,
      # total G1,
      BLS.g1_to_args(key_pair.pub_G1),
      # signing G2
      BLS.g2_to_args(key_pair.pub_G2),
      # total signature
      BLS.g1_to_args(signature),
      # missing partner's G1
      []
    ).call()
    # Assert based on the expected result
    self.assertTrue(pairingSuccessful and siganatureIsValid, 'Signature not verified')

  def test_aggregated_sign_on_contract(self):
    """Aggregated signature should verify by contract"""

    key1 = BLS.create_key_pair()
    key2 = BLS.create_key_pair()

    message = BLS.hash_str("Hello, World!")
    
    sign1 = BLS.sign_short(message, key1)
    sign2 = BLS.sign_short(message, key2)

    # Call a contract function
    [pairingSuccessful, siganatureIsValid] = self.contract.functions.verifySignature(
      # message
      message,
      # total G1,
      BLS.g1_to_args(BLS.aggregate_points([key1.pub_G1,key2.pub_G1])),
      # signing G2
      BLS.g2_to_args(BLS.aggregate_points([key1.pub_G2, key2.pub_G2])),
      # total signature
      BLS.g1_to_args(BLS.aggregate_points([sign1, sign2])),
      # missing partner's G1
      []
    ).call()
    # Assert based on the expected result
    self.assertTrue(pairingSuccessful and siganatureIsValid, 'Aggregated signature not verified')

  def test_missing_partner_by_contract(self):
    """Missing partner should be handle by contract"""

    key1 = BLS.create_key_pair()
    key2 = BLS.create_key_pair()
    # missing partners
    key3 = BLS.create_key_pair()

    message = BLS.hash_str("Hello, World!")
    
    sign1 = BLS.sign_short(message, key1)
    sign2 = BLS.sign_short(message, key2)

    # Call a contract function
    [pairingSuccessful, siganatureIsValid] = self.contract.functions.verifySignature(
      # message
      message,
      # total G1,
      BLS.g1_to_args(BLS.aggregate_points([key1.pub_G1, key2.pub_G1, key3.pub_G1])),
      # signing G2
      BLS.g2_to_args(BLS.aggregate_points([key1.pub_G2, key2.pub_G2])),
      # total signature
      BLS.g1_to_args(BLS.aggregate_points([sign1, sign2])),
      # missing partner's G1
      [BLS.g1_to_args(key3.pub_G1)]
    ).call()
    # Assert based on the expected result
    self.assertTrue(pairingSuccessful and siganatureIsValid, 'Aggregated signature with missing partner not verified')





# class TestMCLLibrary(unittest.TestCase):

#   def test_sign_and_verify(self):
#     """Sign & verify should work"""
    
#     # key_pair = BLS.create_key_pair()
#     key_pair = BLS.create_key_pair(b"123456")
#     message = BLS.hash_str("Hello, World!")
#     message2 = BLS.hash_str("dummy text")
#     signature = BLS.sign_short(message, key_pair)
#     # verified = BLS.verify_short("dummy message".encode('utf-8'), signature, key_pair.pub_G2)
#     self.assertTrue(BLS.verify_short(message, signature, key_pair.pub_G2))
#     self.assertFalse(BLS.verify_short(message2, signature, key_pair.pub_G2))

#   def test_aggregation(self):
#     """Signature aggregation should work"""

#     key1 = BLS.create_key_pair()
#     key2 = BLS.create_key_pair()

#     message = BLS.hash_str("Hello, World!")

#     sign1 = BLS.sign_short(message, key1)
#     sign2 = BLS.sign_short(message, key2)

#     verified = BLS.verify_short(
#       message,
#       sign1 + sign2,
#       key1.pub_G2 + key2.pub_G2
#     )

#     self.assertTrue(verified)

if __name__ == '__main__':
  unittest.main()