nums = []
res = []

nums.append(input())
nums.append(input())
nums.append(input())

n = len(nums)

# initial res to 1
for i in range(n):
    res.append(1)

for num in nums:
    
    res = res * float(num)

print(res)