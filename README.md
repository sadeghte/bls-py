# BLS Signature Library

Sign &amp; verify messages using BLS signature to be verified on the ethereum smart contracts.


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

#### Test
```
$ python3 -m unittest -v tests.test_mcl_library

```

