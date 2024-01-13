#sha bruteforce
import hashlib
pieces = [
    'da2b128800d4e129def769b7ec5decc00517fa8b',
    '602c57ffb51af99d6f3b54c0ee9587bb110fb990',
    '6d4551f349867cc4b06a84feee7bf1db4e2e76bb',
    '20e2daeeb6e61c0aef789bc6851a635b55ca25cd',
    '875b7eeb1fae1be28d54e7c7e71b7674f29dde05',
    '094b0fe0e302854af1311afab85b5203ba457a3b',
    'd312cc75dc28ced757eef6ec22a7e3706905e352',
    '46fb40a57e2f84c82d147545979d164ecc9b2adb',
    'a00ea9f63976ded011afda187adbeccdc2a22a25',
    'c2f26cf0d7c959ad6ea2e8332a54923fa6b378d2',
    'df211ccdd94a63e0bcb9e6ae427a249484a49d60',
    'd42929a8e629463cc7d3c859bdc8e25db35d6963',
    'ceca32e904728d1645727cb2b9cdeaa153807d77',
    '5efb4ac2212f109ebc889dc2a735f791dfc4119a',
    '600ccd1b71569232d01d110bc63e906beab04d8c',
    'e42ac444dece0e82f6a1cc1bd69ad86320799403',
    '63617a37a0c977f9ca2ade8a90a62d670b92685a',
    '65fe0fa368590c720491b848829e4c8c8e15c9e9',
    '76cd06466d098060a9eb26e5fd2a25cb1f3fe0a3',
    'b504c843b2ef4c55c673be0b1daf3b12c5cf2fe8',
    'cd1b646ebd1f6844c60dd91951c6867e43857114',
    'b1c1d8736f20db3fb6c1c66bb1455ed43909f0d8',
    '1dd76b4e93e1d1e1eefc363df7625b205566acf0',
    'b452d6b23b3c28f85872fffd99bdaf90ce0ad44a',
    'f85b7725bf05b838b389fd7726d9b68049c38517',
    'c387c982a132d05cbd5f88840aef2c8157740049',
    '6951a7d0b292e378a802bea446b18e351b14e839'
  ]
  
  
def cracker(hashed):
    for i in range(127):
        for j in range(127):
            trial = chr(i) + chr(j)
            res = hashlib.sha1(trial.encode("utf-8")).hexdigest()
            if res == hashed:
                return trial

    print('Failed to crack the hash: ' + hashed)


def main():
    decoded = ''
    for i in pieces:
        decoded += cracker(i)
    print(decoded)


if __name__ == "__main__":
    main()