import sys; sys.stdin = open('1316그룹단어찾기.txt')

def check(word):
    visited = [0] * 27

    for i in range(len(word) - 1):

        convert = ord(word[i]) - 96
        if not visited[convert]:
            visited[convert] = 1

            if i == len(word) - 2 and word[i] == word[i + 1]:
                return 1

            elif i == len(word) - 2 and not visited[ord(word[i + 1]) - 96]:
                return 1

            elif i == len(word) - 2 and visited[ord(word[i + 1]) - 96]:
                return 0


        else:
            if word[i] != word[i - 1] and word[i] != word[i + 1]:
                return 0

    if visited[ord(word[-1]) - 96] and word[i] != word[i + 1]:
        return 0

    return 1




n = int(input())
result = 0
for i in range(n):
    word = input()
    result += check(word)

print(result)