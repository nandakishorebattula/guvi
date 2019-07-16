    
a,b=input().strip().split(" ")
b=int(b)
i=0
while i<len(a)-1 and b:
	if(a[i]>a[i+1]):
		b-=1
		a=a[:i]+a[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
v=n[:len(a)-b]
print(v)
