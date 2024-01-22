class Solution(object):
    def __init__(self,x):
        self.x = x
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x) # 將整數x轉為字串
        for i in range(len(x)//2):  # 使用迴圈遍歷字串的前半部，由於後半部為對稱，所以不須再檢查一次
            if x[i] != x[-i-1]: # 檢查正序、到序的兩個位置是否相等，如果都相等，則回傳True，如果沒有則回傳False
                return False
        return True    
        


if __name__ =='__main__':
    x = -141
    a = Solution(x)
    result = a.isPalindrome(x)
    print(result)
