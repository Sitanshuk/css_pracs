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

class Multiplicative:
	def encode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(letter * key)%26 + ord('A') for letter in text]
		return ''.join(chr(i) for i in temp)

	def decode(text,key):
		text = [ord(letter) - ord('A') for letter in text]
		temp = [(letter * modinv(key))%26 + ord('A') for letter in text]
		return ''.join(chr(i) for i in temp)

encoded_text = Multiplicative.encode('Sitanshu Kushwaha',19)
print(encoded_text)

decoded_text = Multiplicative.decode(encoded_text,19)
print(decoded_text)



