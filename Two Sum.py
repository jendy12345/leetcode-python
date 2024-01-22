class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} #key: diff ,value:index
        #用一個array跑整個function
        for idx, num in enumerate(nums): #用enumerate可同時得到index和value
            if diff.get(num, None) == None: #檢查現在這個整數不再dictionary裡面的話，就要用現在這個整數和目標和的差當作這個dictionary的key整合起來
                diff[target-num]=idx
            else:
                return [diff[num],idx]

            
