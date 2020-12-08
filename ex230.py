def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
# 왼쪽: 200
# 오른쪽: 300 이 출력된다.
# my_print(a,b)함수를 정의하였다. 정의 내용은 print("왼쪽:", a)와 print("오른쪽:", b)이다.
# 이때 my_print(a,b)와 print("왼쪽:", a), print("오른쪽:", b)에서의 a,b는 다르다.
# 즉, 왼쪽: 과 a=200이므로 왼쪽: 200이 출력되고, 오른쪽: 과 b=100이므로 오른쪽: 100이 출력된다.