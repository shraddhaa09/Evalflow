nums=[55,22,11,99,77]

largest=nums[0]
i=0

while i<len(nums):
    if nums[i]>largest:
        largest=nums[i]
    i=i+1

print(largest)