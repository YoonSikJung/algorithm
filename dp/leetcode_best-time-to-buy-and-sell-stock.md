

## 문제(⭐️)
leetcode: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

<img src = ../images/leetcode_best-time-to-buy-and-sell-stock.png width="500">
 
## 풀이 설명
기본적인 dp문제에 이전 배열 중 최소값만 가지고 있으면 되는 문제이다.  
현재 날짜에서 가장 비싸게 팔수 있는 경우의 수는 아래와 같다. 
1. 직전 날의 이익(지금까지의 최고 이익)
2. 현재 날짜에서 구할 수 있는 이익

1번과 2번 중 큰 값으로 계속해서 업데이트하면 마지막 값이 가장 큰 이익을 나타낸다.

## 코드
```python
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		max_price = [0] * n
		my_min = prices[0]
		
		for i in range(1, n) :
			max_price[i] = max(prices[i]-my_min , max_price[i-1])
			my_min = min(my_min, prices[i])
		
		return max_price[n-1]
```
