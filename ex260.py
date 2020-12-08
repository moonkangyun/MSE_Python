class OMG : 
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
# 에러가 발생한 이유는 print함수를 인자가 없게 정의하였는데 mystock.print()를 쓰면 파이썬에서는 OMG.print(mystock)이라고 인지하기 때문에 인자가 생기므로 에러가 발생한다.
# 에러가 발생하지 않기 위해서는 print함수를 정의할때 def print(self): 라고 하여야한다.