"""
Given a list_of_ints, find the highest_product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""


def highest_prod_of_3(nums):
    highest = max(nums[:2])
    lowest = min(nums[:2])

    highest_prod_2 = lowest_prod_2 = nums[0] * nums[1]
    highest_prod_3 = highest_prod_2 * nums[2]

    for num in nums[2:]:
        highest_prod_3 = max(
            highest_prod_3,
            lowest_prod_2 * num,
            highest_prod_2 * num)

        highest_prod_2 = max(
            highest_prod_2,
            num * highest,
            num * lowest)
        
        lowest_prod_2 = min(
            lowest_prod_2,
            num * highest,
            num * lowest)

        highest = max(num, highest)
        lowest = min(num, lowest)
    return highest_prod_3


def highest_prod_of_n(nums, prod_num=3):
    lowest_prod_n = [min(nums[:prod_num - 1]) for _ in range(prod_num)]
    highest_prod_n = [max(nums[:prod_num - 1]) for _ in range(prod_num)]

    for n in range(prod_num + 1, -1, -1):
        for num in nums[prod_num - 1:]:
            highest_prod_n[n] = max(highest_prod_n[n], num)
            lowest_prod_n[n] = min(lowest_prod_n[n], num)
            if n > 0:
                highest_prod_n[n] = max(
                    highest_prod_n[n],
                    num * highest_prod_n[n - 1],
                    num * lowest_prod_n[n - 1])
                lowest_prod_n[n] = min(
                    lowest_prod_n[n],
                    num * highest_prod_n[n],
                    num * lowest_prod_n[n])
    return highest_prod_n[prod_num]

if __name__ == '__main__':
    nums = [3, 5, 6, 10, 15]
    assert highest_prod_of_3(nums) == (6 * 10 * 15)
    print('[+] Test #1 passed')

    nums = [-10, -5, 1, 3, 2, 10]
    assert highest_prod_of_3(nums) == (-10 * -5 * 10)
    print('[+] Test #2 passed')

    nums = [4, -8, 3, 5, 1, -2, 3, 6]
    assert highest_prod_of_3(nums) == (6 * 4 * 5)
    print('[+] Test #3 passed')
