sum = 0
i = 0

while i<11:  # i변수를 1부터 시작해서 10까지 10번 반복
    i = i + 1
    if i % 2 == 0: # 나머지 연산자 %, 2로 나누어서 나머지가 0이면 짝수
        print("i = ", i)
        sum = sum + i
    else:
        continue

print("sum = ", sum)
