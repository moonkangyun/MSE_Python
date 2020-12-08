import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#btc에서 데이터를 리스트화해서 가져오고 변동폭을 최고가와 최저값의 차이로 정의하기 위해서 btc의 데이터를 가져와 실수형으로 변환해준다. 똑같이 시가와 최고가를 float함수를 이용하여 실수형으로 변환해준다.
#다음에는 if함수를 이용하여 시가+변동폭이 최고가 보다 높으면 상승장 그렇지 않다면 하락장으로 if문을 짠다.