import sys; sys.stdin = open('트리순회.txt')

t = int(input())
tree = {}
for i in range(t):
    root, left, right = input().split()
    tree[root] = (left, right)
# print(tree)

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

preorder('A')
print()

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

inorder('A')
print()


def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node,end='')


postorder('A')

















#
#
# sys.setrecursionlimit(10**6)
# def preorder(node):
#     if node == '.':
#         return
#     print(node, end = "")
#     preorder(tree[node][0])
#     preorder(tree[node][1])
#
# def inorder(node):
#     if node == '.':
#         return
#     inorder(tree[node][0])
#     print(node, end = "")
#     inorder(tree[node][1])
#
# def postorder(node):
#     if node == '.':
#         return
#     postorder(tree[node][0])
#     postorder(tree[node][1])
#     print(node, end = "")
#
#
# n = int(input())
# tree = {}
#
# # make tree
# for _ in range(n):
#     root, left, right = input().split()
#     tree[root] = (left, right)
#     print(tree)
#
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
#
#
#
#
#
#













# arr = [0]*(2**(n-2))
# print(arr)
# for _ in range(n):
#     V, L, R = input().split()
#
#     arr[1] = 'A'
#     if V == 'A':
#         arr[2] = L
#         arr[3] = R
#         print(arr)
#
#     else:
#         i = arr.index(V)
#         arr[2 * i] = L
#         arr[2 * i + 1] = R
#
# print(arr)
#
# for i in range(2**(n-3)):
#     if arr[i] == '.' or '0':
#         pass
#     else:
#         print(arr[i], end='')
#
#     if arr[2 * i] == '.':
#         pass
#     else:
#         print(arr[2 * i], end='')
#
#     if arr[2 * i + 1] == '.':
#         pass
#     else:
#         print(arr[2 * i + 1], end='')
#





