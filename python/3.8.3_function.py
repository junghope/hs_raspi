def sum(math, eng, kor):
    return (math+eng+kor)

score = [90, 80, 100]
print("sum=", sum(*score))# sum(90, 80, 100) 과 같음

