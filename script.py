nums = [3, 3]
target = int(input("Введите число: "))
for n0, i in enumerate(nums, 0):
    for n1, j in enumerate(nums[n0 + 1:], n0 + 1):
        if i + j == target:
            print(n0, n1)

