����������

# 1������
num=0
while 1:
	if num==10:
		print(10)
		break
	if num%2==0:
		print(num)
	num=num+1
	continue

#2. 2������
num=0
for num in range(0,11):
	if num%2==0:
		print(num)
	else :
		continue


#3. 3������

def positive(x): 
    return x > 0

print(list(filter(positive, [1,-3,2,0,-5,6])))



�λ繮��
# 1������
a= [12,78,6,94,587,156,789,481,567,74,12444]
for i in a:
	if i%3==0:
		print("%d�� 3�� ����Դϴ�"%i)

# 2������
text="""���ֵ����� ���� ������ ���� �����ϱ��?
1. ����
2. ����
3. ����
4. �̽�Ʈ����Ʈ
5. ����īī��
6. ��

������?"""
num=0
while num!=6:
	print(text)
	num=int(input())



�縸 �븮�� ����
# 1������
def IsLeapYear(inYear):
	if inYear%100==0:
		print('������ �ƴմϴ�')
	if inYear%4==0:
		print('�����Դϴ�')
	else :
		print('������ �ƴմϴ�')

