import sys
from unittest import result

#a는 들어오는 문자열을 한글자씩 나눠 리스트로 변환해준다
a = list(map(str, sys.stdin.readline().rstrip()))

#for문으로 a 리스트에 있는 문자들을 아스키코드 숫자로 변환해 새로운 리스트를 만든다.
num_list = []
for i in a:
    num_list.append(ord(i))

#새로운 리스트의 숫자들이 알파벳 소문자 숫자 범위 내에 있는것과 밖에 있는 것을 구분한다.
result = []
#알파벳소문자는 아스키코드상 97과 122사이에 있다. 
#아래의 포문은 a부터 z까지 숫자를 순회한다.
for i in range(97,123):
    #해당하는 숫자(알파벳)이 인풋값에 있는 알파벳이라면
    if i in num_list:
        #인풋값의 index위치를 리스트에 더한다
        result.append(num_list.index(i))

    #해당하는 숫자(알파벳)이 인풋값에 없는 알파벳이라면    
    else:
        #-1을 넣는다
        result.append(-1)

#문제에서 원하는 형태로 출력한다
print(*result)
