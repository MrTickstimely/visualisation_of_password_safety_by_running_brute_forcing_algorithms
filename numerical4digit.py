#brute force password searching

#searching for a 4 digit pass

tarr=input("enter your password ")
tarr1=int(tarr)
x=0
while x!=tarr1:
	x=x+1
print(f"your password by using while loop is {x} ")
for i in range(1000,9999):
	if i==tarr1:
		break
		
print(f"your password by using for loop is {i} ")














