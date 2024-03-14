"""
LeetCode206: 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1:
输入:head = [1,2,3,4,5]
输出:[5,4,3,2,1]

示例 2:
输入:head = [1,2]
输出:[2,1]

示例 3:
输入:head = []
输出:[]
 
提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
     
"""
此代码已通过leetcode测试
击败98%
"""   
def reverseList(head):
    if not head:
        return None
    pre_node, current_node, next_node = None, head, head.next
    current_node.next = pre_node
    while next_node:
        pre_node = current_node
        current_node = next_node
        next_node = next_node.next
        current_node.next = pre_node
    return current_node

"""
这是翻转链表的递归实现
击败99%
"""
def reverse_list_recursion(head):
    if not head or not head.next:
        return head
    next_node = reverse_list_recursion(head.next)
    head.next.next = head
    head.next = None
    return next_node


"""本地测试代码
通过数组数据来构建链表
并打印反转后的链表
"""
# 构建一个链表：1 -> 2 -> 3 -> 4 -> 5
nums = [1, 2, 3, 4, 5, 6, 7, 9]
# node_list = []

def generate_list(nums):
    node_list = []
    # 先生成孤立节点
    for num in nums:
        node_list.append(ListNode(num, None))
    # 将孤立的链表节点连接起来
    for i in range(len(node_list)-1):
        node_list[i].next = node_list[i+1]
    # 返回表头元素即可
    return node_list[0] 


def print_list_node(head):
    print_list = []
    current_node = head
    while current_node:
        print_list.append(current_node.val)
        current_node = current_node.next
    print(print_list)

# for num in nums:
#     node_list.append(ListNode(num))
# for i in range(len(node_list) - 1):
#     node_list[i].next = node_list[i+1]

# 将链表进行反转
newHead = reverse_list_recursion(generate_list(nums))
print_list_node(newHead)

# 打印反转后的链表：5 -> 4 -> 3 -> 2 -> 1
# current_node = newHead
# while current_node:
#     print(current_node.val, end=" ")
#     current_node = current_node.next


        