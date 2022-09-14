class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        print(d)
        for a,b in d.items():
            freq[b].append(a)
        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)