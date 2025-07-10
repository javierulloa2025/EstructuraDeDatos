"""Necesitamos encontrar dos índices en un arreglo de números enteros tales que 
los números en esos índices sumen un valor objetivo específico. 
La solución debe ser eficiente y no usar el mismo elemento dos veces."""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                 return [i, j]
        return []


s = Solution()

nums=[2,7,11,15]
target = 9
print(s.twoSum(nums,target))



