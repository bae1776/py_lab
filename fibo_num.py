#!/usr/bin/python

n = int(input('fibbonacci number? '))

first=1
second=1
third=2

for i in range(n):
	if i < 2:
		print('1', end=',')
	else:
		third = first+second
		print('{}'.format(third), end=',');
		first = second
		second = third

print('\b ') #뒤에 남은 콤마 지우고 개행

print('F{} = {}'.format(n, third)) 
