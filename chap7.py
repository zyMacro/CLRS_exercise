def partition(A,p,r):
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
def quicksort(A,p,r):
	if p<r:
		q=partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)

A=[1,5,3,6,7,2,9,10]
p=0
r=7
quicksort(A,p,r)
for i in range(0,8):
	print A[i]
