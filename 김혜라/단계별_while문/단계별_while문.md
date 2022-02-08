# 단계별_while문 

----

---



## 1110. 더하기 사이클 

#### 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

#### 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

#### 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

#### N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

첫째 줄에 N의 사이클 길이를 출력한다.

``` python
26 #4

55 #3

1  #60

0  #1

71 #12
```

n이 10보다 작은경우와 10보다 큰 경우를 나눴다. 10보다 작은 경우 front = N을 할당했다. 그리고 back에는 int('0' + N) 을 할당했다. 

``` python
front = 0
back = 0
if int(N)<10:
    front = '0' + N #09
    back = N #9
    new_num = front[-1] + back[-1] #99
    print(new_num) #99
    print(int(new_num[0]) + int(new_num[1])) #18
    new_num = int(new_num[0]) + int(new_num[1])
    count += 1
    
else:
    front = str(new_num)[-1] #8
    back = int(str(new_num)[0]) + int(str(new_num)[1]) #9
```

10보다 작은 수 9를 넣어보자. 9를 넣으면 앞에 0이 붙어 front는 09가 되고, back은 9가 되어야 하지만 어짜피 10보다 작은 수와 0을 더하면 back의 오른쪽 자리는 변동이 없기 때문에 N을 그대로 넣어줬다. 지금의 N은 맵을 통해 int로 변환하지 않았기 때문에 여전히 문자열이고, 그러므로 슬라이싱을 이용할 수 있다. 



0 + 9 = 9 new_num = 18 

1 + 8 = 9 new_num = 89

8 + 9 = 17 new_num = 97

9 + 7 = 16 new_num = 76

7 + 6 = 13 new_num = 63

6 + 3 = 9 new_num = 39

3 + 9 = 12 new_num = 92

9 + 2 = 11 new_num = 21

2 + 1 = 3 new_num = 13

1 + 3 = 4 new_num = 34

3 + 4 = 7 new = 47

4 + 7 = 11 new 71

7 + 1 = 8 new 18

1 + 8 = 9 new 89



``` python
import sys
N = sys.stdin.readline().rstrip()

new_num = N
count = 0
front = 0
back = 0
while new_num != int(N):
    if len(new_num) < 2:
        front = '0' + N
        back = N
        new_num = front[-1] + back[-1]
        new_num = int(new_num[0]) + int(new_num[1])
        count += 1

    else:
        front = str(new_num)[-1] 
        back = str(int(str(new_num)[0]) + int(str(new_num)[1]))
        new_num = front + back
        count += 1

print(count)
```

``` python
N = input()

new_num = N
count = 0
if int(new_num) < 10:
    front = '0' + N
    back = N
    new_num = front[-1] + back[-1]
    new_num = int(new_num[0]) + int(new_num[1])
    count += 1

while new_num != int(N):
    
    front = str(new_num)[-1] 
    if int(new_num) >= 10:
        back = str(int(str(new_num)[0]) + int(str(new_num)[1]))
    else:
        back = str(int(str(new_num)[0]))
    if back == N:
        print(count)
        break
    count += 1
    new_num = int(front + back[-1])
    

print(count)
```

