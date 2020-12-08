ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
result = 0
i = 0
for row in ohlc[1:]:
    result = result + (row[3] - row[0])
    i = i + 1
    print(i,"일차 수익", result, "원")
print("총수익", result, "원")
#result 초기값을 0으로 둔다.
#row함수와 for문을 이용해서 ohlc에서 [100, 110, 70, 100],[200, 210, 180, 190],[300, 310, 300, 310] 의 값들을 빼낸다.
#수익을 알기 위해서 리스트 에서 제일 끝숫자에서 제일 앞 숫자를 빼야하므로 row[3] - row[0]을 쓴다.
#이렇게 구한 수익을 result에 더하고 for문이 끝나고 나서의 값을 알기위해 for문 밖에 print함수를 쓴다.