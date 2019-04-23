def modinv(key,mod = 26):
	r1 = mod
	r2 = key
	t1 = 0
	t2 = 1
	r = 1 #any dummy value except 0 will work
	while r!=0:
		q = int(r1/r2)
		r = r1%r2
		t = t1 - q*t2
		r1 = r2
		r2 = r
		t1 = t2
		t2 = t
	return t1

class Affine:
	def encode(text,key):
		a,b = key
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(a*letter + b)%26 + ord('A') for letter in text]
		return ''.join(chr(i) for i in temp)

	def decode(text,key):
		a,b = key
		text = [ord(letter) - ord('A') for letter in text]
		temp = [(modinv(a)*(letter - b))%26 + ord('A') for letter in text]
		return ''.join(chr(i) for i in temp)

encoded_text = Affine.encode("Cryptography",(9,2))
print(encoded_text)
decoded_text = Affine.decode(encoded_text,(9,2))
print(decoded_text)