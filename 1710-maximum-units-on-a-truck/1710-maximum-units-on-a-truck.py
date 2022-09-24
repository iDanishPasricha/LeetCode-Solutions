class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes,key = lambda x: x[1] , reverse=True)
        print(boxTypes)
        ans = 0
        boxes = 0

        for i in boxTypes:
            if i[0]+boxes <= truckSize:
                ans+= i[1]*i[0]
                boxes+=i[0]

            else:
                ans += (truckSize-boxes)*i[1]
                boxes+= (truckSize-boxes)
                break

        return ans