from hashlib import sha256
import random
import re

num = random.getrandbits(256)
while True:
    has = sha256(str(num).encode()).hexdigest()

    if re.search(r"\b[a-z0-9]{5}0e[0-9]{23,}", has) is not None:
        print(num)
        print(has)

        break

    # randomize num again
    num = random.getrandbits(256)
