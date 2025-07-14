from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode()  # 虚拟头节点
        current = dummy
        carry = 0  # 进位

        while l1 or l2 or carry:
            # 获取当前位的值
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 计算和与进位
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # 移动指针
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # 返回结果链表的头节点


def main():
    solution = Solution()

    # 构造测试用例：l1 = [2, 4, 3], l2 = [5, 6, 4]
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    # 调用方法并打印结果
    result = solution.addTwoNumbers(l1, l2)

    # 打印结果链表
    while result:
        print(result.val, end=" ")
        result = result.next
    print()  # 输出: 7 0 8

if __name__ == "__main__":
    main()