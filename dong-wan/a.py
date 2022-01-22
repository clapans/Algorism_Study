def solution(numbers, hand):
    answer = ''
    if numbers[0] in [2,5,8,0]:
        if hand == 'left':
            answer += 'L'
        else :
            answer += 'R'
        for num in numbers[1:len(numbers)]:
            if num in [1,4,7]:
                answer+= 'L'
            elif num in [3,6,9]:
                answer += 'R'
            else :
                if answer[-1] == 'L' :
                    answer += 'L'
                else :
                    answer += 'R'
    else :
        for num in numbers:
            if num in [1,4,7]:
                answer+= 'L'
            elif num in [3,6,9]:
                answer += 'R'
            else :
                if answer[-1] == 'L' :
                    answer += 'L'
                else :
                    answer += 'R'
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))