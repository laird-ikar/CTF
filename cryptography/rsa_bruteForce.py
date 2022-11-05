#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import rsa
import math
import string
import itertools

def encrypt(message, key):
	return int.from_bytes(rsa.encrypt(message.encode('ascii'), key), 'little')

def generateStrings(i):
	return [i]

def arr_to_str(s):
	new = ""
	for x in s:
		new += x
	return new

key = rsa.PublicKey( 0xddf57b7634051da953ec321067cdc7bb7f95842fc834738e0a8d71224ed64b4ba38b69b107be86f2fe0c1c03541c2c951ba852799e3b94baebd1248b706228331b3cb7fcb62e4493beeb5a59bbbf42a0ac846118bd5e1065e31b4b8c916ae814746669328a234de8b90dc49e98bd7a46c528da87e45ab61083d828fe1f27e00dd98980c8d5d57256cc3e7877a0600e91528f45bd524c2f8d320abe4d5f1a0690123d8036038308d55f44bab94504e1ed495d501e4e32a134f67c2afc5f0929de52b87043a611f8c50a1e6e7bfe30f32d1e2fe55d83bb7c94c974587e38324008b8ec24f3272bc6dedc0fc7f1978f9f8c9095426b519fd5521bb692c88bbd6be3, 0x03)

chars = string.printable

for i in range(2048):
	print(i)
	for arr in itertools.product(chars, repeat=i):
		if (encrypt(arr_to_str(arr), key) == 0x1811ca69474cf7dce163acd43dc99520d94c98de9fab1da5285c53795bcc77451af202566bb90aad9921448ce1eec7b26e1b67d0c6b89a26ccc87f925d19db825f36d4cbc9077eaa2b17219ed24260d02f6af94a56f7c14980e27cfa38e3710dcfcbd1944ed7370032432504347c82ce9e9d):
			print (arr)
			exit()

# rsa.encrypt("test".encode('utf8'), key)
