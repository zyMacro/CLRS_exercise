#leetcode 258
def add(num):
	a=[]
	b=0
	while num>=10:
		a.append(num%10)
		num=num/10
		print num
	a.append(num)
	print 'i:'
	for i in a:
		print i
		global b
		b=b+i
	if b<10:
		return b
	else:
		add(b)

add(128)
b=0
print 'final score:'
print b
