class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
# 자식생성
# 부모생성 이 출력된다.
# 부모 클래스를 만들고 __init__(self)라는 생산자를 만든다.
# 그다음 자식 클래스를 만들고 똑같이 생산자를 만든다. 그 후 super()함수를 통해 부모 클래스에 접근한다.
# 나 = 자식()으로 인해 자식생성이 먼저 출력이 되고 super().__init__()에 의해서 부모생성이 출력된다.