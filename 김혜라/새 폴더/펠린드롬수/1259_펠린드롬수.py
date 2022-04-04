import sys;sys.stdin = open('iinput.txt')

def pelin(num):
    while len(num) >= 2:
        if num[0] == num[-1]:
            num = num[1:-1]
        else:
            return False
    return True

while True:
    n = input()

    if n == '0':
        break
    # print(n)
    if pelin(n):
        print('yes')
    else:
        print('no')



