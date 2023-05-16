# 言葉 Kotoba - Words


This script helps you calculate a mnemonic seed using a coin, a dice or whatever flips and has faces.

Follow the instructions and it will prints you the words that form your mnemonic seed.


The english wordlist is embedded in base64 in the script, you can verify the SHA256 hash using the original wordlist:
```
https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
```

This table shows how number of faces, base and number of throws are related.

| 1024 | 512  | 256  | 128  |  64  |  32  |  16  |  8   |  4   |  2   |  1   | total | faces | base | throws |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ----: | ----: | ---: | -----: |
|    1 |    1 |    1 |    1 |    1 |    1 |    1 |    1 |    1 |    1 |    1 |  2047 |     2 |    2 |     11 |
|    1 |    - |    3 |    - |    3 |    - |    3 |    - |    3 |    - |    3 |  2047 |     4 |    4 |      6 |
|    1 |    - |    3 |    - |    3 |    - |    3 |    - |    3 |    - |    3 |  2047 |     6 |    4 |      6 |
|    - |    3 |    - |    - |    7 |    - |    - |    7 |    - |    - |    7 |  2047 |     8 |    8 |      4 |
|    - |    3 |    - |    - |    7 |    - |    - |    7 |    - |    - |    7 |  2047 |    10 |    8 |      4 |
|    - |    3 |    - |    - |    7 |    - |    - |    7 |    - |    - |    7 |  2047 |    12 |    8 |      4 |
|    - |    - |    7 |    - |    - |    - |   15 |    - |    - |    - |   15 |  2047 |    20 |   16 |      3 |
|  ... |  ... |  ... |  ... |  ... |  ... |  ... |  ... |  ... |  ... |  ... |   ... |   ... |  ... |    ... |


The following table describes the relation between the initial entropy length (ENT), the checksum length (CS), and the length of the generated mnemonic sentence (MS) in words. 
```
CS = ENT / 32
MS = (ENT + CS) / 11
```
| ENT |  CS  | ENT+CS |  MS  |
| --- | ---: | -----: | ---: |
| 128 |    4 |    132 |   12 |
| 160 |    5 |    165 |   15 |
| 192 |    6 |    198 |   18 |
| 224 |    7 |    231 |   21 |
| 256 |    8 |    264 |   24 |