""" 
LeetCode 316: 去除重复字母
题目：
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"

提示：
●1 <= s.length <= 104
●s 由小写英文字母组成
"""

""" 
去除重复字母的算法
"""
def remove_duplicate_letters(s):
    stack = []
    s_dict = {value: i for i, value in enumerate(s)}
    for i, value in enumerate(s):
        if value in stack: continue
        while stack and value < stack[-1] and s_dict[stack[-1]] > i:
            stack.pop()
        stack.append(value)
    return "".join(stack)

s = "abacdcbc"
#s = "bcabc"
s = "cbacdcbc"
print(remove_duplicate_letters(s))