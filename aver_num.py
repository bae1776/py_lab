#!/usr/bin/python


#1. 몇 개 숫자를 입력할지 물어보기
num=int(input("how Many numbers? : "))
total=0

for element in range(num):
#2. num만큼 반복하며 값을 입력받아 총합에 더함
	total+=int(input())

#3. 평균 계산 및 출력
print(total/num)
