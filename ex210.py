def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#B
#C
#B
#C
#B
#C
#A 가 나올것이다.
#def message1(): 함수를 이용하여 message1()을 출력하면 A가 나오고 똑같이 message2()는 B를 출력하게 정의하였다.
#def message3()에서는 for문과 range함수를 이용해서 변수 i로 message2와 c 출력을 3번 반복하게 하였고 3번 다했을 때 message1을 출력하라하였다.
#그러므로 순서대로 BCBCBC 다음에 A가 나온다.