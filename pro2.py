p,q=input().strip().split(" ")
q=int(b)
sum=0
while(sum<len(p)-1 and q):
  if(p[sum]>p[sum+1]):
    q-=1
    p=p[:sum]+p[sum+1:]
    if(sum!=0):
      sum-=1
  else:
    sum+=1
d=p[:len(p)-q]
print(d)
