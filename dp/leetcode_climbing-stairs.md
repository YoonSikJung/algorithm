

## 문제(⭐️)
leetcode: [Climing Stairs](https://leetcode.com/problems/climbing-stairs/)

<img src = ../images/leetcode_climbing-stairs.png width="500">
 
## 풀이 설명
dp의 대표적인 문제로 볼 수 있을 것 같다.  
해당 계단을 오르는 방법은 바로 직전의 계단에서 한 칸을 움직이는 경우와 전전 칸의 계단에서 2 step을 뛰는 방법이 있다. 

## 코드
```python
class Solution:
	def climbStairs(self, n):
		a = [0] * (n+1)
		if n <= 2 : return 1 if n==1 else  2
		a[1], a[2] = 1,2
		for i in range(3, n+1) :
			a[i] = a[i-1] + a[i-2]
			
		return a[n]

```
