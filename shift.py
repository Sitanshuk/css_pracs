class shift:
	def encode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(letter + key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp ])

	def decode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		temp = [(letter - key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp ])

encoded_text = shift.encode('SFIT',7)
print(encoded_text)

decoded_text = shift.decode(encoded_text,7)
print(decoded_text)