class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        bed = [0]+bed+[0]
        for i in range(1,len(bed)-1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                n-=1
                bed[i] = 1
        return n<=0
            