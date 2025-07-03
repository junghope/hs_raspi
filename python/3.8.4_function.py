def sum(*scores):
    sum = 0
    for arg in scores:# 가변인자 값은 for문 사용해서
        sum = sum + arg
        
    return (sum)

print("sum=", sum(30,40,80,90))# 4개의 인자 전달
print("sum=", sum(30,40,80))# 3개의 인자 전달

