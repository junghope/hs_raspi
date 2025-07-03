sum = 0
i = 1

while i<11:    # i변수를 1부터 시작해서 10까지 10번 반복
    sum = sum + i
    print("i = ", i)
    if( i == 5 ) : break  # 반복 중에 i가 5가되면 while 루프를 빠져 나감
    i = i + 1

print("sum = ", sum)
