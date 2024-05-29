VERIFIER_CONTRACT_ABI = [
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "msgHash",
        "type": "bytes32"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "X",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "Y",
            "type": "uint256"
          }
        ],
        "internalType": "struct BN254.G1Point",
        "name": "apk",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256[2]",
            "name": "X",
            "type": "uint256[2]"
          },
          {
            "internalType": "uint256[2]",
            "name": "Y",
            "type": "uint256[2]"
          }
        ],
        "internalType": "struct BN254.G2Point",
        "name": "apkG2",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "X",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "Y",
            "type": "uint256"
          }
        ],
        "internalType": "struct BN254.G1Point",
        "name": "sigma",
        "type": "tuple"
      }
    ],
    "name": "trySignatureAndApkVerification",
    "outputs": [
      {
        "internalType": "bool",
        "name": "pairingSuccessful",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "siganatureIsValid",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "msgHash",
        "type": "bytes32"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "X",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "Y",
            "type": "uint256"
          }
        ],
        "internalType": "struct BN254.G1Point",
        "name": "apkG1",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256[2]",
            "name": "X",
            "type": "uint256[2]"
          },
          {
            "internalType": "uint256[2]",
            "name": "Y",
            "type": "uint256[2]"
          }
        ],
        "internalType": "struct BN254.G2Point",
        "name": "apkG2",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "X",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "Y",
            "type": "uint256"
          }
        ],
        "internalType": "struct BN254.G1Point",
        "name": "sigma",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "X",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "Y",
            "type": "uint256"
          }
        ],
        "internalType": "struct BN254.G1Point[]",
        "name": "nonSignerPubkeys",
        "type": "tuple[]"
      }
    ],
    "name": "verifySignature",
    "outputs": [
      {
        "internalType": "bool",
        "name": "pairingSuccessful",
        "type": "bool"
      },
      {
        "internalType": "bool",
        "name": "siganatureIsValid",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]