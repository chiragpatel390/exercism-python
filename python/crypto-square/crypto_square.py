
from math import ceil, sqrt

def encode(plain_text):
	
	for ch in [',','.','!','@','%',' ']:
		plain_text=plain_text.replace(ch,'')

	plain_text=plain_text.lower()

	c=ceil(sqrt(len(plain_text)))

	if len(plain_text)<(c*(c-1)):
		r=c-1
	else:
		r=c

	plain_text = plain_text+' '*((r*c)-len(plain_text))

	rectangle=[]
	count=r
	start=0
	end=c
	while count>0:
		rectangle.append(plain_text[start:end])
		start+=c
		end+=c
		count-=1

	encoded=''

	for i in range(c):
		for code in rectangle:
			encoded+=code[i]
		if i!=(c-1):
			encoded+=' '

	return encoded