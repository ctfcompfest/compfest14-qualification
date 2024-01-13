import hashlib
import binascii
import base58
from bit import Key
import itertools
from bitcoin import pubkey_to_address

#source https://github.com/j4rj4r/Bitcoin-Brainwallet-Bruteforce/blob/main/privatekey.py
class PrivateKey:
    def __init__(self, privatekey=None):
        self.privatekey = privatekey
        self.passphrase = None
        self.wif = None

    def from_passphrase(self, passphrase):
        hex_private_key = hashlib.sha256(passphrase.encode('utf-8')).hexdigest()
        self.privatekey = hex_private_key
        self.passphrase = passphrase
        self.wif = None
        return self.privatekey

    def privatekey_to_wif(self, privatekey=None, compressed=False):
        if privatekey is None:
            privatekey = self.privatekey
        else:
            privatekey = privatekey
        if compressed:
            extented_key = "80" + privatekey + "01"
        else:
            extented_key = "80" + privatekey
        first_sha256 = hashlib.sha256(binascii.unhexlify(extented_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extented_key + second_sha256[:8]
        wif = base58.b58encode(binascii.unhexlify(final_key))
        wif = wif.decode("utf-8")
        self.wif = wif
        return wif

charset = ['i', 'n', 'd', 'o', 'e', 's', 'a']
pubkey = '04983fdc0830be5654449592f2d3957edf4cdf3240b1045e5727cc1784446f7b35e65eb81969234dd667e1fbd56d92ae23fa57b4d1000738c6583ee41c292ba05e'
bitcoin_address = pubkey_to_address(pubkey)
wallet =PrivateKey()

for password in itertools.product(charset, repeat=9):
    pw = ''.join(password)
    wallet.from_passphrase(pw)
    wif = wallet.privatekey_to_wif()
    if (str(Key(wif))[13:-1] == bitcoin_address):
        print(wif)
        print(pw)
        break

