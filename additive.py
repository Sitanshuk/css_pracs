class additive:
	def encode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(letter + key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp ])

	def decode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(letter - key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp ])

encoded_text = additive.encode('Sitanshu Kushwaha',15)
print(encoded_text)

decoded_text = additive.decode(encoded_text,15)
print(decoded_text)