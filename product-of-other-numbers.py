"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

    [1, 7, 3, 4]

your function would return:

    [84, 12, 28, 21]

by calculating:

    [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""
import operator
import functools


def get_product_of_other_nums(nums):
    prods_except_idx = [1 for num in nums]

    nnums = len(nums)
    product_so_far = 1
    for idx in range(nnums):
        prods_except_idx[idx] = product_so_far
        product_so_far = product_so_far * nums[idx]

    product_so_far = 1
    for idx in range(nnums - 1, -1, -1):
        prods_except_idx[idx] = prods_except_idx[idx] * product_so_far
        product_so_far = product_so_far * nums[idx]

    return prods_except_idx


if __name__ == '__main__':

    nums = [1, 7, 3, 4]
    assert get_product_of_other_nums(nums) == [84, 12, 28, 21]

    #nums = [3, 1, 2, 5, 6, 4]
    #assert get_product_of_other_nums(nums) == [1, 3, 3, 6, 30, 180]
    
    print('[+] Tests passed.')
