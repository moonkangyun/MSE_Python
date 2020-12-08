date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price)) # zip함수를 이용하여 따로 존재하는 리스트 들을 하나로 만들어주고 dict()함수를 이용하여 하나로 모은 리스트를 딕셔너리화 시켜준다.
print(close_table)