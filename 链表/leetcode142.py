"""
题目:
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1, 则在该链表中没有环。注意: pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。


示例 1:
输入: head = [3,2,0,-4], pos = 1
输出: 返回索引为 1 的链表节点
解释: 链表中有一个环，其尾部连接到第二个节点。

示例 2:
输入: head = [1,2], pos = 0
输出: 返回索引为 0 的链表节点
解释: 链表中有一个环，其尾部连接到第一个节点。

示例 3: 
输入: head = [1], pos = -1
输出: 返回 null
解释: 链表中没有环。
 

提示:
链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 
进阶: 你是否可以使用 O(1) 空间解决此题？ 
"""

from list_node import ListNode


"""
创建一个循环链表
最后一个节点连接到倒数第K个节点
"""
def create_cycle_list(nums, k):
    dummy = ListNode(0)
    current_node = dummy
    for num in nums:
        new_node = ListNode(num)
        current_node.next = new_node
        current_node = new_node
    last_node = current_node
    counts = 0
    current_node = dummy.next
    length = len(nums) - 1
    while counts < length - k:
        counts += 1
        current_node = current_node.next
    last_node.next = current_node
    
    return dummy.next


"""
检测环的入口节点
返回：入口节点 
"""
def detect_cycle(head):
    if not head or not head.next:
        return None
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            slow = head
            while slow != fast:
                fast, slow = fast.next, slow.next
            return slow
    return None
    
    
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#nums = [3, 2, 0, -4]
head = create_cycle_list(nums, 8)
# count = 0
# while count < 10:
#     print(head.val, end = " ")
#     head = head.next
#     count += 1
# print(" ")
print(detect_cycle(head).val)
