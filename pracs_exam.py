
class Additive:	
	#key value can be a variable and is same as SHIFT cipher
	def encode(text, key):
		text = [ord(i) - ord('A') for i in text.replace(' ','').upper()]
		temp = [(letter + key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])


	def decode(text, key):
		text = [ord(i) - ord('A') for i in text]
		temp = [(letter - key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])

class Caesar:
	#key value is fixed as key = 3
	def encode(text):
		key = 3
		text = [ord(i) - ord('A') for i in text.replace(' ','').upper()]
		temp = [(letter + key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])


	def decode(text):
		key = 3
		text = [ord(i) - ord('A') for i in text]
		temp = [(letter - key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])

class Shift(Additive):
	#same as Additive cipher
	pass

class Multiplicative:
	def modInverse(a, m) : 
		#temp 1 is the table on left side of Euclidean method 
		temp1 = [[int(m/a)], [m], [a], [m%a]]
		while temp1[2][-1] != 1:
			try:
				temp1[1].append(temp1[2][-1])
				temp1[2].append(temp1[3][-1])
				temp1[0].append(int(temp1[1][-1]/temp1[2][-1]))
				temp1[3].append(temp1[1][-1]%temp1[2][-1])
			except:
				raise ValueError

		#temp 2 is the table on right side of Euclidean method 
		t = -temp1[0][0]
		temp2 = [[0], [1], [t]]
		for i in range(1,len(temp1[0])):
			t1 = temp2[1][-1]
			temp2[0].append(t1)
			t2 = temp2[2][-1]
			temp2[1].append(t2)
			q = temp1[0][i]
			temp2[2].append(t1 - (q * t2))
		return temp2[1][-1]

		# print(temp1)
	def encode(text,key):
		text = [ord(i) - ord('A') for i in text.replace(' ','').upper()]
		temp = [(letter * key)%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])

	def decode(text, key):
		text = [ord(i) - ord('A') for i in text]
		temp = [(letter * Multiplicative.modInverse(key,26))%26 + ord('A') for letter in text]
		return ''.join([chr(i) for i in temp])	


encoded_text = Multiplicative.encode("Sitanshu Kushwaha",11)
print(encoded_text)

decoded_text = Multiplicative.decode(encoded_text,11)
print(decoded_text)
