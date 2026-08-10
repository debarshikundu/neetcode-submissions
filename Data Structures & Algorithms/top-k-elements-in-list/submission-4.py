class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        freq2 = []
        kElem = []
        def get_freq(num):
            return freq[num]
        for num in nums:
            if num not in freq:
                freq[num] = 1
            freq[num] += 1
        freq2 = list(sorted(freq, key=get_freq, reverse=True))
        for i in range(k):
            kElem.append(freq2[i])
        return kElem
        
