low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
vol = []
for i in range(0,5,1):
    vol.append(high_prices[i] - low_prices[i])
print(vol)
# vol이라는 변수를 아무것도 들어있지 않은 리스트를 만든다.
# 그 다음 for문과 range함수를 이용해서 vol 리스트에 high_prices - low_prices의 값을 집어 넣는다.
# 이때 집어 넣는 값은 변수 i를 이용하여 각 자릿수에 맞는 값을 뺀 값만 넣는다.