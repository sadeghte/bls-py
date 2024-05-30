# BLS Signature Library

Sign &amp; verify messages using BLS signature to be verified on the EigenLayer smart contracts.


### Install system dependencies
It required to [MCL](https://github.com/herumi/mcl) native package be installed.
```
$ git clone https://github.com/herumi/mcl.git
$ cd mcl
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install
```
for more information read the link above.
### Install python dependencies

```
$ pip install -r requirements.txt
```

# Simple Example
```  py
from bls import BLS

key_pair = BLS.create_key_pair()
message = BLS.hash_str("Hello, World!")
signature = BLS.sign_short(message, key_pair)
verified = BLS.verify_short(message, signature, key_pair.pub_G2)
```

# Aggregation Example
```  py
from bls import BLS

key1 = BLS.create_key_pair()
key2 = BLS.create_key_pair()

message = BLS.hash_str("Hello, World!")

sign1 = BLS.sign_short(message, key1)
sign2 = BLS.sign_short(message, key2)

verified = BLS.verify_short(
  message,
  sign1 + sign2,
  key1.pub_G2 + key2.pub_G2
)
```

# Run Unit Test
```
$ python3 -m unittest -v tests.test_mcl_library

```

# Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

# Disclaimer
This library is provided "as is", without warranty of any kind. Use at your own risk.

