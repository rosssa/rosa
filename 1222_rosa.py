지연씨문제

# 1번문제
num=0
while 1:
	if num==10:
		print(10)
		break
	if num%2==0:
		print(num)
	num=num+1
	continue

#2. 2번문제
num=0
for num in range(0,11):
	if num%2==0:
		print(num)
	else :
		continue


#3. 3번문제

def positive(x): 
    return x > 0

print(list(filter(positive, [1,-3,2,0,-5,6])))



로사문제
# 1번문제
a= [12,78,6,94,587,156,789,481,567,74,12444]
for i in a:
	if i%3==0:
		print("%d는 3의 배수입니다"%i)

# 2번문제
text="""제주도에서 가장 유명한 것은 무엇일까요?
1. 배추
2. 딸기
3. 포도
4. 이스트소프트
5. 다음카카오
6. 귤

정답은?"""
num=0
while num!=6:
	print(text)
	num=int(input())



재만 대리님 문제
# 1번문제
def IsLeapYear(inYear):
	if inYear%100==0:
		print('윤년이 아닙니다')
	if inYear%4==0:
		print('윤년입니다')
	else :
		print('윤년이 아닙니다')

