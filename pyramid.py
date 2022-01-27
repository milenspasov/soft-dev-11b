import random

sum1 = 0 #the sum of the nums
m = 100
nums = []
sum2 =0 #helping

for i in range(m):
    num1 = [] 
    for j in range(i+1):
        num1.append(random.randint(0,100))
    nums.append(num1)

sum1 = nums[0][0]

j = 0
for i in range(m-1):
   sum1 = sum1 + max(nums[i+1][j], nums[i+1][j+1])
   if(nums[i+1][j] < nums[i+1][j+1]):
       j = j + 1
      
print(sum1)
