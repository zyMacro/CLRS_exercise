# def find_max_crossing_subarray(prices,low,mid,high):
# 	sum_1=0
# 	sum_2=0
# 	profit_1=-1e100
# 	profit_2=-1e100
# 	max_left=0
# 	max_right=0
# 	for i in range(mid,low,-1):
# 		sum_1+=prices[i]
# 		if sum_1>profit_1:
# 			profit_1=sum_1
# 			max_left=i
# 	for i in range(mid,high):
# 		sum_2+=prices[i]
# 		if sum_2>profit_2:
# 			profit_2=sum_2
# 			max_right=i
# 	return max_left,max_right,profit_1+profit_2

# def find_maximum_subarray(prices,low,high):
# 	if high==low:
# 		return low,high,prices[low]
# 	else:
# 		mid=(high+low)/2
# 		# print 'mid:'+str(mid)
# 		left_low,left_high,left_sum=find_maximum_subarray(prices,low,mid)
# 		right_low,right_high,right_sum=find_maximum_subarray(prices,mid+1,high)
# 		cross_high,cross_low,cross_sum=find_max_crossing_subarray(prices,low,mid,high)
# 		if left_sum>=right_sum and left_sum>=cross_sum:			
# 			print ' 1: '+str(left_sum)+' 2: '+str(right_sum)+' 3: '+str(cross_sum)
# 			return left_low,left_high,left_sum
# 		elif right_sum>=left_sum and right_sum>=cross_sum:
# 			print '2:'+str(right_sum)
# 			return right_low,right_high,right_sum
# 		else:
# 			print '3:'+str(cross_sum)
# 			return cross_low,cross_high,cross_sum

def find_maximum_subarray(prices):
	max_ending_here=0
	max_so_far=0
	for i in prices:
		max_ending_here=max(0,max_ending_here+i)
		max_so_far=max(max_ending_here,max_so_far)
	return max_so_far

prices=[2,-4,9,-3,6,-2,6,7]
print find_maximum_subarray(prices)