리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  a = i.split(".")
  if (a[1] == "h") or (a[1] == "c"):
    print(i)
# i.splt(".")를 변수 a에 넣는다. 그렇다면 a에는 .을 기준으로 intra, h, intra, c ,,, 등이 나올 것이다.
# 이때 if 문을 이용하여 a에 들어가있는 2번째 자리 즉 a[1]의 값이 h나 c가 되면 a를 출력하는 것이다.
# run.py가 출력되지 않은 이유는 run과 py로 나뉘어져있을 때 a[1]이 py이기 때문이다.