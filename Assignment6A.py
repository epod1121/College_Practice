#Assignment6A
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def count_positive(nums):
    count = 0

    for i in nums:
        i = int(i)
        if i >= 0:
            count += 1
    return count


def count_negative(nums):
    count = 0

    for i in nums:
        i = int(i)
        if i < 0:
            count += 1
    return count


nums = input("Enter numbers separated by spaces: ")
numsList = []

for num in nums.split():
    numsList.append(int(num))

print("\nSorted list: ", bubble_sort(numsList))
print("Positive numbers: ", count_positive(numsList))
print("Negative numbers: ", count_negative(numsList))
