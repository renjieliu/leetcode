class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		input1  = ""
		input2 = ""
		
		len1 = 0
		len2 = 0
		
		#for x in l1:
		for i in (l1[0], l1[-1]):
			len1+=1
		
		for i in (l2[0], l2[-1]):
			len2+=1
		
		
		for i in range(len1,-1,-1):
			input1 += str(l1[i])
		#print (input1)
		for j in range(len2,-1, -1):
			input2 += str(l2[j])		
		#print (input2)
		sum = str(int(input1) + int(input2))
		#print(sum)
		r = []
		for i in range(len(sum)-1, -1, -1):
			r.append(int(sum[i]))
		return r

a = [2,4,3]
b = [5,6,4]

# c = Solution()
print(a[::-1]+b[::-1])
 














# class Solution(object):
	# def addTwoNumbers(self, l1, l2):
		# """
		# :type l1: ListNode
		# :type l2: ListNode
		# :rtype: ListNode
		# """
		# input1  = ""
		# input2 = ""
		
		# len1 = 0
		# len2 = 0
		
		# #for x in l1:
		# for i in (l1[0], l1[-1]):
			# len1+=1
		
		# for i in (l2[0], l2[-1]):
			# len2+=1
		
		
		# for i in range(len1,-1,-1):
			# input1 += str(l1[i])
		# #print (input1)
		# for j in range(len2,-1, -1):
			# input2 += str(l2[j])		
		# #print (input2)
		# sum = str(int(input1) + int(input2))
		# #print(sum)
		# r = []
		# for i in range(len(sum)-1, -1, -1):
			# r.append(int(sum[i]))
		# return r

# a = [2,4,3]
# b = [5,6,4]

# c = Solution()
# print(c.addTwoNumbers(a,b))
 
 