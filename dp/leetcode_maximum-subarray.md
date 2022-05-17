

## 문제(⭐️)
leetcode: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

<img src = ../images/maximum-subarray.png width="700">
 
## 풀이 설명
연속된 sub array중에서 합이 가장 큰 경우를 찾는 문제이다.  
이 문제의 핵심은 ```dp[i]는 자신을 포함한 연속된 배열의 합이 큰 경우```이란 것이다.  
점화식은 ```dp[i] = max(nums[i], nums[i]+ dp[i-1])```이다.
이전 dp값(이전 값을 포함하여 최대값의 경우)에 자신을 더한 경우와 오로지 자신만 포함하는 경우를 비교한다.
1번째 배열 요소를 구하는 경우를 생각하면 좀 더 이해가 쉽다.  
0번째 배열은 무조건 nums[0]이다.  
1번째를 구하는 경우 만일 num[0]+num[1]이 num[1]보다 작다면 그냥 num[1]를 저장하면 된다.  
점화식을 이것으로 시작하여 쭉 계산하면 끝난다.


## 코드
```python
class Solution:
	def maxSubArray(self, nums) :
		dp = [0] * len(nums)
		dp[0] = nums[0]
		
		for i in range(1, len(nums)) :
			dp[i] = max(nums[i], nums[i]+ dp[i-1])
		
		return max(dp)
		
```
