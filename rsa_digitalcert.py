from math import gcd
class Rsa:
	def generator(n1,n2):
		n = n1*n2
		phi = (n1-1)*(n2-1)
		for i in range(2,phi):
			if gcd(i,phi) == 1:
				e = i
				break
		k = 0
		while k < 1000:
			if (k * phi + 1)%e == 0:
				d = int((k * phi + 1)/e)
				break
			k += 1
		return((e,n),(d,n))

	def signature(text,key):
		d,n = key
		return (text**d)%n

	def verify(text,key):
		e,n = key
		return (text**e)%n

PublicKey,PrivateKey = Rsa.generator(17,11)
encoded_text = Rsa.signature(25,PrivateKey)
print(encoded_text)

decoded_text = Rsa.verify(encoded_text,PublicKey)
print(decoded_text)
