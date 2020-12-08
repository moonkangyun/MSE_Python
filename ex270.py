class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

종목 = []

삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
	
# 먼저 Stock 클래스를 생성한다. 이 때 객체에 종목명, 종목코드, PER, PBR, 배당수익률의 입력을 받게끔 메서드를 생성자를 놓는다.
# 그리고 텅빈 리스트를 변수 종목으로 둔다.
# 삼성전자, 현대차, LG전자의 종목명, 종목코드, PER, PBR, 배당수익률을 Stock에 넣는다.
# 넣은 값들은 종목 리스트에 넣는다.
# 그리고 for문을 이용해서 code와 PER을 출력한다.