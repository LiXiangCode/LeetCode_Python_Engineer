""" 
题目:
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

示例 1
输入: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出: Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0)。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1,因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，
它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点, B 中第四个节点) 在内存中指向相同的位置。
 

示例 2
输入: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出: Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3
输入: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出: null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
 

提示：
listA 中节点数目为 m
listB 中节点数目为 n
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
 

进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
"""
from list_node import ListNode

"""
创建一个相交链表
指定两个链表从末尾往前数的第几个相交
返回: 两个链表的头结点
"""
def create_intersect_list(nums1, nums2, k):
    dummy1 = ListNode(0)
    dummy2 = ListNode(0)
    lista = dummy1
    listb = dummy2
    for num in nums1:
        new_node = ListNode(num)
        lista.next = new_node
        lista = new_node
    for num in nums1:
        new_node = ListNode(num)
        listb.next = new_node
        listb = new_node   
    
    counts = 1
    lista = dummy1.next
    listb = dummy2.next
    pos1 = len(nums1) - k
    while counts < pos1:
        lista = lista.next
        counts += 1
        
    pos2 = len(nums2) - k
    counts = 1
    while counts < pos2:
        listb = listb.next
        counts += 1    
    
    listb.next = lista.next
    
    return dummy1.next, dummy2.next

""" 
返回两个相交链表的交点
"""
def get_intersection_node(headA, headB):
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA

""" 
测试代码
"""
nums1 = [4, 1, 8, 4, 5]
nums2 = [5, 6, 1, 8, 4, 5]
head1, head2 = create_intersect_list(nums1, nums2, 1)
print(get_intersection_node(head1, head2).val)




