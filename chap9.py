def Randomized_partition(A,p,r):
	x=A[r]
	i=p-1
	for j in range(p,r):
		if A[j]<=x:
			i=i+1
			t=A[j]
			A[j]=A[i]
			A[i]=t
	t=A[r]
	A[r]=A[i+1]
	A[i+1]=t
	return i+1
def Randomized_select(A,p,r,i):
	if p==r:
		return A[p]
	q=Randomized_partition(A,p,r)
	k=q-p+1
	print k
	if i==k:
		return A[q]
	elif i<k:
		return Randomized_select(A,p,q-1,i)
	else:
		return Randomized_select(A,q+1,r,i-k)

A=[9,8,7,6,5,4,3,2,1]
p=0
r=8

i=5
print Randomized_select(A,p,r,i)
