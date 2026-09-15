class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        product: int = reduce(lambda a, b: a * b, nums)
        num_zeros: int = nums.count(0)
        alternative_product: int = 0

        if num_zeros > 1:
            return [0 for _ in nums]
        elif num_zeros == 1:
            alternative_product = reduce(
                lambda a, b: a * b, filter(lambda a: not a == 0, nums)
            )
            return [
                product // num if not num == 0 else alternative_product for num in nums
            ]

        # no zeros
        return [product // num for num in nums]



