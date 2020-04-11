#　单向链表
class Node(object):
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.next = None
        
class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node
        
    def is_empty(self):
        """
        :return 如果链表为空 返回真
        """
        return self.__head == None
    
    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")
    
    def add(self, item):
        """链表头部添加元素
        :param item: 要保存的具体的数据
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node
    
    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 如果链表为空，需要特殊处理
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 退出循环的时候，cur指向的尾节点
            cur.next = node
        
    
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 在头部添加元素
        if pos <= 0:
            self.add(item)
        # 在尾部添加元素
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 退出循环的时候，cur指向pos的前一个位置
            node = Node(item)
            node.next = cur.next
            cur.next = node
    
    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到了要删除的元素
            if cur.item == item:
                # 在头部找到了元素
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            # 不是要找的元素，移动游标
            pre = cur
            cur = cur.next
    
    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
if __name__ == '__main__':
    print("单向链表")
    ll = SingleLinkList()
    print(ll.length())
    ll.travel()
    
    ll.append(1) # 1
    print(ll.length())
    ll.travel()
    
    ll.append(2) # 1  2
    print(ll.length())
    ll.travel()
    
    ll.add(3) # 3  1  2
    ll.travel()
    
    
    ll.insert(0, 4) # 4 3 1 2 
    ll.travel()
    
    
    ll.insert(19, 5) # 4 3 1 2 5
    ll.travel()
    
    ll.insert(2, 6)  # 4  3 6 1 2 5
    ll.travel()
    
    ll.remove(4)  # 3 6 1 2 5
    ll.travel()
    
    
    ll.remove(5)  # 3 6 1 2 
    ll.travel()
    
    
    ll.remove(6)  # 3 1 2 
    ll.travel()
        

    ll.remove(3)  # 1 2 
    ll.travel()
    
    
    ll.remove(2)   # 1
    ll.travel()
    print()
    
    
    ll.remove(1)   # 
    ll.travel()
    
    
