a=int(input())
o=[]
for b in range(0,a):
 c=input()
 o.append(c)
de=[]
for b in zip(*o):
 if(b.count(b[0])==len(b)):
  de.append(b[0])
 else:
  break
print(''.join(de))
