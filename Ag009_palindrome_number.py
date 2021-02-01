class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        tmp = x
        rev = 0
        while x != 0:
            d = x % 10
            rev = rev * 10 + d
            x //= 10
        if rev == tmp:
            return True
        else:
            return False

        

思路：计算x的反序rev，如果和x相等则返回真，否则返回假。
比如10021：
1. 把个位1提取出来，加到rev中 =1，然后对1002进行操作；
2. 把各位2提取出来，加到rev*10中 =1*10+2=12，然后对100进行操作
3. 把各位0提取出来，加到rev*10中 =12*10+0=120，然后对10进行操作
4. 把各位0提取出来，加到rev*10中 =120*10+0=1200，然后对1进行操作
5. 把各位1提取出来，加到rev*10中 =1200*10+1=12001，结束
