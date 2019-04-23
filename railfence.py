from math import ceil, floor
class Railfence:
	#for key = 2 
	def encode(text):
		text1 = [letter for i,letter in enumerate(text) if i%2==0]
		text2 = [letter for i,letter in enumerate(text) if i%2!=0]
		return ''.join(text1+text2)

	def decode(text):
		
		text1 = text[:ceil(len(text)/2)]
		print(text1)
		text2 = text[ceil(len(text)/2):]
		print(text2)
		temp = ''

		for i, val1 in enumerate(text1):
			for j, val2 in enumerate(text2):
				if i==j:
					temp += val1+val2

		#to handle plain text of odd length also			
		if len(text)%2 != 0:
			temp += text1[-1]
		return temp

encoded_text = Railfence.encode('Meet me at the park')
print(encoded_text)

decoded_text = Railfence.decode(encoded_text)
print(decoded_text)
