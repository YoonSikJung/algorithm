

## 문제(⭐️⭐️)
프로그래머스: [정수 삼각형](https://programmers.co.kr/learn/courses/30/lessons/43105)

<img src = ../images/programmers_43105.png width="500">
 
## 풀이 설명
특정 줄을 실행 할 때, 윗줄을 참고하여 max값으로 업데이트한다.  
각 라인을 새롭게 구할 때 미리 전 라인에서 최대값을 구하게 되어 memoization을 시행했다고도 볼 수 있겠다.

## 코드
```python
def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)) :
        triangle[i][0] +=  triangle[i-1][0]

        for j in range(1, len(triangle[i])-1) :
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])

        triangle[i][len(triangle[i])-1] +=  triangle[i-1][len(triangle[i-1])-1]

    return max(triangle[len(triangle)-1])
```
