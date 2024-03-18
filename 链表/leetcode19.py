"""
leetcode19: 删除链表中的倒数第N个节点
题目：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
示例 1:
输入: head = [1,2,3,4,5], n = 2
输出: [1,2,3,5]

示例 2:
输入: head = [1], n = 1
输出: []

示例 3:
输入: head = [1,2], n = 1
输出: [1]
 
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class ListNode(object):
    def __init__(self, nums):
        assert(len(nums) >= 1)
        self.val = nums[0]
        self.next = None

        node = self
        for num in nums[1:]:
            node.next = ListNode([num])
            node = node.next  
            
    def print_list_node(self):
        if self:
            current_node = self
            while current_node:
                print(f"{current_node.val}->", end = "")
                current_node = current_node.next
                
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    current, node_list = head, []
    while current:
        node_list.append(current)
        current = current.next
    length = len(node_list)
    position = length - n
    if length <= 1:
        return None
    if position == 0:
        node_list[0].next = None
        return node_list[1]
    elif position == length - 1:
        node_list[position-1].next = None
    else:
        node_list[position-1].next = node_list[position-1].next.next
        node_list[position].next = None
    return node_list[0]


nums = [1, 2, 3, 4, 5, 6, 7, 9]
nums = [1, 2]
nums = [1, 2, 3, 4, 5]
head = ListNode(nums)
head = removeNthFromEnd(head, 2)
while head:
    print(head.val, end = " ")
    head = head.next   

# head.print_list_node()