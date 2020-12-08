def print_max(a, b, c):
	if a > b and a > c:
	    print(a)
	elif b > a and b > c:
	    print(b)
	else:
	    print(c)
print_max(a,b,c)
# print_max함수를 if문으로 정의한다.
# if문의 내용은 a가 b와 c보다 크면 a를 출력하고 그렇지않으면 b가 a와 c보다 크다면 b를 출력, 이것도 아니라면 c를 출력하라는 것이다.