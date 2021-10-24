from cryptography import __version__
from cryptography.cryptography import *

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual = encrypt("I Like Python", 6)
    expected = "o roqk veznut"
    assert actual == expected

def test_decrypt():
    actual = decrypt("o roqk veznut", 0)
    expected = "o roqk veznut"
    assert actual == expected 

def test_crack():
    actual = crack(encrypt("I Like Python", 3))
    expected = "i like python"
    assert actual == expected

