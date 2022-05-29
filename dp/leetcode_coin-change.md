## 문제(⭐️⭐️⭐️)
leetcode: [Coin Change](https://leetcode.com/problems/coin-change/)

<img src = ../images/leetcode_coin-change.png width="700">
 
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2<sup>31</sup> - 1
- 0 <= amount <= 10<sup>4</sup>

## 풀이 설명
이번 문제의 dp 식은 현재 코인을 `포함하여` 만들 수 있는 경우이다.  
시간 복잡도는 len(coins)\*amount으로 볼 수 있고, 12\*amount이므로 결국 O(n*amount)로 보면 될 것 같다.  


### 잘못된 접근
처음 문제를 접근 할 때 dp[i]는 아래과 같이 구현을 하였다.
```python
for j in range(1, i//2+1) :
    if dp[j]!=-1 and dp[i-j]!=-1 :
        tmp.append(dp[j]+dp[i-j])
if len(tmp) != 0 :
    dp[i] = min(tmp)
```
위와 같은 코딩은 amount*(amount/2) 즉, O(n<sup>2</sup>/2)으로 볼 수 있을 것 같다.  
최악의 경우 10<sup>4</sup>*10<sup>4</sup>/2로 타임아웃 될 확률이 높다.


## 코드
```python
class Solution:
    def coinChange(self, coins, amount) -> int:
        if amount == 0 : return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1)  :
            
            for j, val in enumerate(coins) :
                if i - val >= 0 :
                    dp[i] = min( dp[i], dp[i-val]+1)

        return dp[amount] if dp[amount]!=float('inf') else -1
```

## 새로 배운 것
파이썬에는 무한대를 표시할 수 있다.  
```float('inf')```로 표시할 수 있다.  
만일 음의 무한대를 표시하고 싶으면 ```float('-inf')```로 표시하면 된다.  
최대값, 최소값을 세팅하거나 혹은 비교를 할 때 사용하면 편할 것 같다.