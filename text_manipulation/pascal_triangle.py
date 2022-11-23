while True:
    n = input("Enter number of rows: ")
    if n.startswith("q"):
    	break
    elif not n.isdigit():
    	print("{} is not an integer".format(n))
    	break
    else:
    	n = int(n)
    	if n > 100:
    		s = input("Warning: very high number. Do you want to continue anyway (y/n)? ")
    		if not s.startswith("y"):
    			break
    a = []
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()
    print()