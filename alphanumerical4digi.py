alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9"]
tarr=input("please enter your password")
for x1 in alpha:
	for x2 in alpha:
		for x3 in alpha:
			for x4 in alpha:
				guess= x1+x2+x3+x4
				if guess==tarr:
					print(f"{guess}")
					break
