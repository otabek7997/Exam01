nums = []

for i in range(6):
    num = input(f'{i+1}-son: ')
    nums.append(num)

max_num = nums[0]
min_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num

for num in nums:
    if num < min_num:
        min_num = num

print(max_num)
print(min_num)         