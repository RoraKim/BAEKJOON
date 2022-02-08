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

