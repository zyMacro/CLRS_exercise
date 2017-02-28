s='hello'
a=[]
b=[]
for i in s:
	a.append(i)
	
for i in range(1,len(a)+1):
	
	b.append(a[-i])
	
s=('').join(b)
print s
# for j in s:
# 	print j