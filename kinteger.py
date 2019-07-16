p,q=input().split()
p=int(p)
q=int(q)
r=list(map(int,input().split()))[:p]
sum=0
for i in range(q):
	sum=sum+r[i]
print(sum)
