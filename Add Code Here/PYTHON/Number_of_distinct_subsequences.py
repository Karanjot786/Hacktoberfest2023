# GFG problem
# Link: https://practice.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1

# Solution:

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends

class Solution:
    def distinctSubsequences(self, S):
        # code here
        n = len(S)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = {}
        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            if S[i - 1] in last:
                dp[i] -= dp[last[S[i - 1]]]
            last[S[i - 1]] = i - 1
        return dp[n] % 1000000007
