### 문제(⭐️⭐️⭐️)
*백준 사이트는 테스트 케이스 입력까지 고려를 해야한다.  
개인적으로 별로 썩 좋아하지는 않는다...*  
백준: [퇴사](https://www.acmicpc.net/problem/14501)

<img src = ../images/backjoon_14501.png width="800">

### 풀이
dp[i]는 i번째 이후에 받을 수 있는 최대 금액을 담고 있으면 된다.  
dp[i] = max(dp[t[i]+i] + p[i], max_value)로 볼 수 있다.  
정리하자면 **바로 전의 값이 자신 이후에 최대임을 보장한다.**

### 코드

```python
n = int(input())

t_list = []
p_list = []
answer = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n-1, -1, -1) :
    dp[i] = max(dp[i+t_list[i]] + p_list[i], dp[i+1]) if i + t_list[i] <= n else  dp[i+1]

print(dp[0])
```
