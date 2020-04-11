# 栈
class Stack(object):
    """栈"""
    def __init__(self):
        self.__items = []
        # self.__items = SingleLinkList()
        
    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__items.append(item)      # O(1)
#         self.__items.insert(0, item) # O(n)
        
    def pop(self):
        """弹出栈顶元素"""
        self.__items.pop()
#         self.__items.pop(0) 

    def peek(self):
        """返回栈顶元素"""
        return self.__items[-1]
        #  return  self.__items[len(self.__items)-1]
     
    def is_empty(self):
        """判断栈是否为空"""
        return self.__items == []
    
    def size(self):
        """返回栈的元素个数"""
        return len(self.__items)
        
        
