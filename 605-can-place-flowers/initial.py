from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        listLen = len(flowerbed)
        addFlowers = 0
        for i, v in enumerate(flowerbed):
            pV = 0
            nV = 0
            if v == 0:
                if i > 0:
                    pV = flowerbed[i - 1]
                if i < listLen - 1:
                    nV = flowerbed[i + 1]
                if pV == 0 and nV == 0:
                    addFlowers += 1
                    flowerbed[i] = 1
        return addFlowers >= n
