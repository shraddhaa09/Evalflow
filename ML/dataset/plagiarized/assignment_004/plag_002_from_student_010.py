nums = [90, 40, 70, 10]

n = len(nums)

for i in range(n-1):
    for j in range(n-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("Sorted elements are")
print(nums)