def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
# 28 이 나온다.
# 함수0(num)을 return num * 2라고 정의하였다.
# 함수1(num)을 return 함수0(num + 2)라고 정의하였다.
# 다시말해 함수1(num)은  num + 2한 값에 * 2 한 것을 return하는 함수다.
# 함수2(num)은 num = num + 10과 return 함수1(num)으로 정의하였다.
# 즉 함수2(num)은 주어진 num 에 10을 더하고 그 값을 함수1에 넣는다.
# c=함수2(2)이므로 함수2에 num = 2를 넣는다. 그 값은 10을 더해 12가 되고 그 값을 다시 함수1에 넣는다.
# 그럼 num + 2이므로 14가 다시 함수0에 들어가고 그 값이 2배가 되므로 print(c) = 28이 된다.