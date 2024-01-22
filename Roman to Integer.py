class Solution(object):
    def __init__(self,s):
        self.s = s

    def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman = {'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,}
        for i in range(len(s)): # 會遍歷所有字串s，而每個索引由i表示
            if(roman[s[i]]): # 判斷字典roman中的s[i]對應的值是否存在
                temp = roman[s[i]] # 將字典中s[i]對應到的阿拉伯數字存到temp
                if i != 0 and roman[s[i-1]] < roman[s[i]]: # 檢查目前處理的羅馬數字s[i]，是否大於前一個羅馬數字s[i-1]的對應值，如果是，則會減去前一個羅馬數字的兩倍
                    temp = temp - (roman[s[i-1]])*2 # temp減去前一個羅馬數字的兩倍
                result += temp # 最後將調整好的temp累加並存result中
        return result

if __name__ == '__main__':
    s = 'III'
    result = Solution(s)
    a = result.romanToInt(s)
    print(a)
