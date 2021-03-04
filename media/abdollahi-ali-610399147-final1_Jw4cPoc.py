def power(k,t):
    answer = 1

    for i in range(t):
        answer *= k
    return answer
i , j = map(int,input().split())
answer = 0
for k in range(i):
    for t in range(j):
        answer += power(k,t)
print(answer)