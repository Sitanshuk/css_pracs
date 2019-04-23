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
	if t1 < 0:
		t1 = t1 + mod
	return t1

class Hill:
	def encode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		key = [ord(letter) - ord('A') for letter in key.replace(' ','').upper()]
		if len(text)%2 != 0:
			text.append(23)
		mat_text = [text[i:i+2] for i in range(0,int(len(text)),2)]
		mat_key = [key[i:i+2] for i in range(0,int(len(key)),2)]
		mat_ans = list()
		for i in range(len(mat_text)):
			temp = list()
			for j in range(len(mat_key[0])):
				value = 0
				for k in range(len(mat_key)):
					value  += mat_text[i][k]*mat_key[k][j]
				temp.append(value%26)
			mat_ans.append(temp)
		encoded_text = ''.join([chr(j + ord('A')) for i in mat_ans for j in i])
		return encoded_text

	def decode(text,key):
		text = [ord(letter) - ord('A') for letter in text.replace(' ','').upper()]
		mat_text = [text[i:i+2] for i in range(0,int(len(text)),2)]

		mat_key = [	[15*19,8*19],
					[11*19,19*19]]
		mat_ans = list()
		for i in range(len(mat_text)):
			temp = list()
			for j in range(len(mat_key[0])):
				value = 0
				for k in range(len(mat_key)):
					value  += mat_text[i][k]*mat_key[k][j]
				temp.append(value%26)
			mat_ans.append(temp)
		decoded_text = ''.join([chr(j + ord('A')) for i in mat_ans for j in i])
		return decoded_text

encoded_text = Hill.encode('short','hill')
print(encoded_text)

decoded_text = Hill.decode(encoded_text,'hill')
print(decoded_text)

