def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer = sorted(answer)
    
    if answer == []:
        answer.append(-1)