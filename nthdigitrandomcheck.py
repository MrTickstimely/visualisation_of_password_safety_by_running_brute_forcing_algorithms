#checking how many instances it takes for a randomly generated 4 digit number to match exactly with another randomly generated 4 digit number
import random 
n=input("how many digits should the number have?")
n1=int(n)
word2="l"
word31="p"
count=0
while word2!=word31:

	word=""
	for i in range(n1):
		a=random.randint(0,9)
		a2=str(a)
		word=word+a2	
	word2=int(word)

	word21=""
	for j in range(n1):
		b=random.randint(0,9)
		a21=str(b)
		word21=word21+a21	
	word31=int(word21)
	
	
	count=count+1
print(f"the algorithm has finally generated two same {n1} digit numbers after ",count,"attempts.")	