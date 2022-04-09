def solution(brown, yellow):
    answer = []

    x = 3
    while True :
        y = 3
        while True :

            nb = x*2 + y*2 - 4
            ny = (x-2) * (y-2)

            if nb > brown or ny > yellow :
                break

            if nb == brown and ny == yellow:
                answer.append(x)
                answer.append(y)
                answer.sort(reverse=True)
                return answer

            y += 1
        x += 1

    return answer
