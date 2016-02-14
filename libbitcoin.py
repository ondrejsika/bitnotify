import requests
from bip32utils import BIP32Key


def satoshi_to_btc(sat):
    return float(sat) / 10**8


def get_balance(address):
    return requests.get('https://blockchain.info/q/addressbalance/%s' % address).json()


def get_last_tx_id(address):
    raw_address = requests.get('https://blockchain.info/address/%s?format=json&limit=1&offset=0' % address).json()
    return raw_address['txs'][0]['hash']


def get_txs_count(address):
    raw_address = requests.get('https://blockchain.info/address/%s?format=json&limit=1&offset=0' % address).json()
    return len(raw_address['txs'])


def get_wallet_from_xpub(xpub, no):
    return BIP32Key.fromExtendedKey(xpub).ChildKey(0).ChildKey(no).Address()


def short(s, begin, end):
    return s[:begin]+'..'+s[-end:]
