"""
链表的定义
根据数组创建一个链表 
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def create_list(nums):
    dummy = ListNode(0)
    current_node = dummy
    for num in nums:
        new_node = ListNode(num)
        current_node.next = new_node
        current_node = new_node
    return dummy.next