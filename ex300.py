per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("half")
    finally:
        print("complete")

# per이라는 리스트에서 for문을 이용하여 try함수로 실수라면 실수를 출력하고 else함수와 finally함수로 인해 half와 complete를 출력한다.
# 그다음 다시 for문이므로 10.31, 공백, 8.00에 대해서 모두 수행을 하는데 공백은 실수가 아니므로 예외에 해당한다.
# 즉 0일 때는 except함수가 사용되어 0이 출력되고 half는 출력되지 않는다.