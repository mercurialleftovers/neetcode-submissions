class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict[int, int] = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        tuples: list[tuple(int, int)] = []
        for key, v in frequencies.items():
            tuples.append((key, v))

        tuples.sort(key=lambda duo: duo[1], reverse=True)
        return [key for (key, _) in tuples[:k]]

