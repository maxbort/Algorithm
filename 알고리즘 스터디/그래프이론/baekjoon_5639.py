# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class B_T:
#     def __init__(self):
#         self.root = None
#     def insert(self, value):
#         if not self.root:
#             self.root = Node(value)
#         else:
#             self.insert_re(self.root, value)
        
#     def insert_re(self,current,value):
#         if value < current.value:
#             if current.left is None:
#                 current.left = Node(value)
#             else:
#                 self.insert_re(current.left,value)
#         elif value > current.value:
#             if current.right is None:
#                 current.right = Node(value)
#             else:
#                 self.insert_re(current.right, value)
#         else:
#             pass
#     def search_post(self):
#         answer = []
#         self.search_post_re(self.root, answer)
#         return answer
    
#     def search_post_re(self,current,answer):
#         if current is not None:
#             self.search_post_re(current.left,answer)
#             self.search_post_re(current.right, answer)
#             answer.append(current.value)


# if __name__ == "__main__":
#     b_t = B_T()
#     cnt = 0
#     while True:
#         try:
#             n = int(input())
#             b_t.insert(n)
#         except:
#             break
#     result = b_t.search_post()
#     for i in result:
#         print(i)    


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = []
while True:
    try:
        n.append(int(input()))
    except:
        break
    # 배열의 가장 첫번째 수는 무조건 최상위 루트
    # tmp = n[0]
    # right_idx = 0
    # for i in range(len(n)):
    #     if  n[i] > tmp:
    #         right_idx = i
    # left_idx = 1
    # left_tree = n[1:right_idx]
    # right_tree = n[right_idx:]
    
def post_order(left,right):
    if left > right:
        return
    
    tmp = n[left]
    div = right + 1 # 이 부분에서 시간 오래걸림 씨부레
    for i in range(left + 1, right+1):
        if n[i] > tmp:
            div = i
            break
    post_order(left+1, div-1)
    post_order(div, right)
    print(n[left])

post_order(0,len(n)-1)
    






















