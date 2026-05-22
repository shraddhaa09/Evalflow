nums=[55,22,11,99,77]

big=nums[0]
i=0

while i<len(nums):
    if nums[i]>big:
        big=nums[i]
    i=i+1

print(big)