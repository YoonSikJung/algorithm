# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    if not len(numbers) :
        return 1 if not target else 0
    return solution(numbers[1:],target-numbers[0]) \
            + solution(numbers[1:], target+numbers[0])

