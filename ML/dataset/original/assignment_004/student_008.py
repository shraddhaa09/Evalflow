nums = [8, 6, 4, 2, 9]

count = len(nums)

for i in range(count):
    for j in range(count-i-1):
        if nums[j] >= nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in nums:
    print(i, end=" ")